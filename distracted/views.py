from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib import messages

import urllib
import tempfile
import zipfile
from xml.dom import minidom

from .models import Series
    

class IndexView (generic.ListView):
    template_name = 'distracted/index.html'
    context_object_name = 'series_list'

    def get_queryset (self):
        return Series.objects.order_by('name')

class DetailView (generic.DetailView):
    model = Series
    template_name = 'distracted/detail.html'

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
            id          = self.parseTag("id", node)
            name        = self.parseTag("SeriesName", node)
            banner      = self.parseTag("banner", node)
            overview    = self.parseTag("Overview", node)
            firstAired  = self.parseTag("FirstAired", node)
            network     = self.parseTag("Network", node)
            rating      = self.parseTag("Rating", node)
            ratingCount = self.parseTag("RatingCount", node)
            status      = self.parseTag("Status", node)
            runtime     = self.parseTag("Runtime", node)
            lastUpdate  = self.parseTag("lastupdated", node)
            results.append( {'id'       : id,
                             'name'     : name,
                             'banner'   : banner,
                             'overview' : overview,
                             'firstAired' : firstAired,
                             'network'  : network,
                             'rating'   : rating,
                             'ratingCount' : ratingCount,
                             'status'   : status,
                             'runtime'  : runtime,
                             'lastUpdate' : lastUpdate} )
        return results

    def get(self, request, seriesid):
        try:
            data, actors = self.getData(seriesid)
            #    parse xml string
            domData   = minidom.parseString(data)
            domActors = minidom.parseString(actors)
            #    create DOM Objects for series and episode data
            seriesNodes  = domData.getElementsByTagName("Series")
            episodeNodes = domData.getElementsByTagName("Episode")
            seriesData = self.parseSeries (seriesNodes)
            return render (request, 'distracted/searchDetail.html', {"series" : seriesData[0]})
        except urllib.error.HTTPError as e:
            HttpResponse ("HTTP Error: " + str(e.code) + str(url))
        except urllib.error.URLError as e:
            HttpResponse ("URL Error: " + str(e.reason) + str(url))
        return HttpResponse("You chose id: #%s" % seriesid)
