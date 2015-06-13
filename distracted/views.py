from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

import urllib
import tempfile
import zipfile
from xml.dom import minidom

from .models import Series, Season, Episode, Actor, Roles


def IndexView (request):
    return render (request, 'distracted/index.html')

class SeriesList (generic.ListView):
    template_name = 'distracted/seriesList.html'
    context_object_name = 'series_list'

    def get_queryset (self):
        return Series.objects.order_by('name')
    
class SeriesListBanners (SeriesList):
    template_name = 'distracted/seriesListBanners.html'

class SeriesDetail (generic.DetailView):
    model = Series
    template_name = 'distracted/seriesDetail.html'
    
    #    Override function to get Episode data into the django Context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SeriesDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the episodes
        series = self.get_object()
        context['episodes'] = Episode.objects.filter(series_id=series).order_by("season_id__seasonNumber", "episodeNumber")
        context['roles'] = Roles.objects.filter (series = series).order_by("sort_order", "name");
        return context
    
class SeriesDelete (generic.DetailView):
    model = Series
    template_name = 'distracted/index.html'
    
    def get (self, request, pk):
       object = super(SeriesDelete, self).get_object()
       message = "This series got removed from the database: " + str(object.id) + ", " + object.name 
       messages.info(request, message)
       object.delete()
       return render(request, self.template_name)

def SearchSeries (request):
    return render (request, 'distracted/searchSeries.html')

class SearchResult (generic.View):
    def parseTag (self, tagname, node):
        try:
            result = node.getElementsByTagName(tagname)[0].firstChild.nodeValue
        except:
            result = ""
        return result;

    def parseSeries (self, seriesList):
        results = []
        for node in seriesList:
            id          = self.parseTag("seriesid", node)
            name        = self.parseTag("SeriesName", node)
            alias       = self.parseTag("AliasNames", node)
            banner      = self.parseTag("banner", node)
            overview    = self.parseTag("Overview", node)
            firstAired  = self.parseTag("FirstAired", node)
            network     = self.parseTag("Network", node)
            results.append( {'id'       : id,
                             'name'     : name,
                             'alias'    : alias,
                             'banner'   : banner,
                             'overview' : overview,
                             'firstAired' : firstAired,
                             'network'  : network} )
        return results

    def post (self, request):
        if 'seriesName' in request.POST and request.POST['seriesName']:
            #    create URL
            params = urllib.parse.urlencode({'seriesname': request.POST['seriesName']})
            url = "http://thetvdb.com/api/GetSeries.php?%s" % params

            #    load data from url
            with urllib.request.urlopen(url) as f:
                contents = f.read().decode('utf-8')
            xmldom = minidom.parseString(contents)

            #    check if something was found
            SeriesList = xmldom.getElementsByTagName("Series") 
            if not Series:
                messages.error(request, "No TV Series was found with %s!" % params)
                return HttpResponseRedirect('/distracted/search/')
            #    parse XML and render results
            results = self.parseSeries(SeriesList)
            return render(request, 'distracted/searchResult.html',
                {'seriesList' : results})
        else:
            messages.error(request, "You submitted an empty form!")
            return HttpResponseRedirect('/distracted/search/')

    def get (self, request):
        messages.error(request, "How dare you try to GET me")
        return HttpResponseRedirect('/distracted/search/')

class SearchDetail (generic.View):
    def getData (self, seriesid):
        url = "http://thetvdb.com/api/20EE1583110A3BA2/series/%s/all/en.zip" % seriesid
        local_filename, headers = urllib.request.urlretrieve(url)
        archive = zipfile.ZipFile(local_filename, "r")
        xmldata = archive.read("en.xml")
        xmlactors = archive.read("actors.xml")
        return (xmldata, xmlactors)
    
    def parseTag (self, tagname, node):
        try:
            result = node.getElementsByTagName(tagname)[0].firstChild.nodeValue
        except:
            result = ""
        return result;
    
    def parseSeries (self, domSeries):
        results = []
        for node in domSeries:
            series_id   = self.parseTag("id", node)
            name        = self.parseTag("SeriesName", node)
            overview    = self.parseTag("Overview", node)
            banner      = self.parseTag("banner", node)
            first_aired = self.parseTag("FirstAired", node)
            network     = self.parseTag("Network", node)
            rating      = self.parseTag("Rating", node)
            voters      = self.parseTag("RatingCount", node)
            status      = self.parseTag("Status", node)
            runtime     = self.parseTag("Runtime", node)
            lastUpdate  = self.parseTag("lastupdated", node)
            results.append( {'series_id': series_id,
                             'name'     : name,
                             'banner'   : banner,
                             'overview' : overview,
                             'first_aired' : first_aired,
                             'network'  : network,
                             'rating'   : rating,
                             'voters'   : voters,
                             'status'   : status,
                             'runtime'  : runtime,
                             'lastUpdate' : lastUpdate} )
        return results
    
    def parseEpisodes (self, domEpisodes):
        results = []
        for node in domEpisodes:
            results.append ({
            'id'              : self.parseTag("id", node),
            'director'        : self.parseTag("Director", node),
            'episodeName'     : self.parseTag("EpisodeName", node),
            'firstAired'      : self.parseTag("FirstAired", node),
            'rating'          : self.parseTag("Rating", node),
            'voters'          : self.parseTag("RatingCount", node),
            'episodeNumber'   : self.parseTag("EpisodeNumber", node),
            'seasonNumber'    : self.parseTag("SeasonNumber", node),
            'season_id'       : self.parseTag("seasonid", node),
            'series_id'       : self.parseTag("seriesid", node)
            })
        return results
    
    def parseActors (self, domActors):
        results = []
        for node in domActors:
            results.append ({
                             'id'       : self.parseTag("id", node),
                             'Image'    : self.parseTag("Image", node),
                             'Name'     : self.parseTag("Name", node),
                             'Role'     : self.parseTag("Role", node),
                             'SortOrder': self.parseTag("SortOrder", node)
                             })
        return results;
    
    def parseAllTheThings (self, seriesid):
        data, actors = self.getData(seriesid)
        #    parse xml string to DOM object
        domData   = minidom.parseString(data)
        domActors = minidom.parseString(actors)
        #    create DOM Objects for series and episode data
        seriesNodes  = domData.getElementsByTagName ("Series")
        episodeNodes = domData.getElementsByTagName ("Episode")
        actorsNodes  = domActors.getElementsByTagName("Actor")
        #    parse DOMs for data, returns lists
        seriesData   = self.parseSeries (seriesNodes)
        episodesData = self.parseEpisodes (episodeNodes)
        actorsData   = self.parseActors (actorsNodes)
        return (seriesData, episodesData, actorsData)

    def get(self, request, seriesid):
        try:
            seriesData, episodesData, actorsData = self.parseAllTheThings(seriesid)
            return render (request, 'distracted/searchDetail.html',
                           {"series" : seriesData[0],
                            "episodes" : episodesData,
                            "actors" : actorsData})
        except urllib.error.HTTPError as e:
            HttpResponse ("HTTP Error: " + str(e.code) + str(url))
        except urllib.error.URLError as e:
            HttpResponse ("URL Error: " + str(e.reason) + str(url))
        return HttpResponse("You chose id: #%s" % seriesid)

class SearchSave (SearchDetail):
    def get (self, request, seriesid):
        seriesData, episodesData, actorsData = self.parseAllTheThings(seriesid)
        s = Series.objects.create (
            series_id   = int(seriesData[0]["series_id"]),
            name        = seriesData[0]["name"],
            overview    = seriesData[0]["overview"],
            banner      = seriesData[0]["banner"],
            first_aired = seriesData[0]["first_aired"],
            network     = seriesData[0]["network"],
            rating      = seriesData[0]["rating"],
            voters      = int(seriesData[0]["voters"]),
            runtime     = int(seriesData[0]["runtime"]),
            lastUpdate  = int(seriesData[0]["lastUpdate"])
            )
        s.save()
        #    save episodes
        for episode in episodesData:
            try:
                season = Season.objects.get(season_id = episode["season_id"])
            except ObjectDoesNotExist as err:
                season = Season.objects.create (
                                       season_id = episode["season_id"],
                                       series_id = s,
                                       seasonNumber = episode["seasonNumber"])
            e = Episode ( id = episode["id"],
                          director = episode["director"],
                          episodeName = episode["episodeName"],
                          firstAired = episode["firstAired"] or None,
                          rating = episode["rating"],
                          voters = episode["voters"],
                          episodeNumber = episode["episodeNumber"],
                          season_id = season,
                          series_id = s)
            #    force insert, otherwise Django will use update if the Series already is saved once
            #    This way, an error get's thrown when the user tries to insert the same series twice
            e.save(force_insert=True)
        #    save actor data
        for actor in actorsData:
            try:
                dbactor = Actor.objects.get(actor_id = actor["id"])
            except ObjectDoesNotExist as err:
                dbactor = Actor.objects.create (
                                               actor_id = actor["id"],
                                               name = actor["Name"])
            r = Roles( actor = dbactor,
                       series = s,
                       name = actor["Role"],
                       sort_order = actor["SortOrder"],
                       image = actor["Image"] )
            r.save(force_insert=True)
        messages.success(request, "TV Series has been saved in the DB")            
        return render (request, 'distracted/searchDetail.html', {"series" : seriesData[0], "episodes" : episodesData})

