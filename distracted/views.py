from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib import messages

import urllib
from xml.dom import minidom

from .models import Series


class IndexView(generic.ListView):
    template_name = 'distracted/index.html'
    context_object_name = 'series_list'

    def get_queryset(self):
        return Series.objects.order_by('name')

class DetailView (generic.DetailView):
    model = Series
    template_name = 'distracted/detail.html'

def SearchSeries (request):
    return render(request, 'distracted/searchSeries.html')

def SearchResult (request):
    if 'seriesName' in request.POST and request.POST['seriesName']:
        #    create URL
        params = urllib.parse.urlencode({'seriesname': request.POST['seriesName']})
        url = "http://thetvdb.com/api/GetSeries.php?%s" % params
        #    load data from url
        with urllib.request.urlopen(url) as f:
            contents = f.read().decode('utf-8')
        xmldom = minidom.parseString(contents)
        #    check if something was found
        if not xmldom.getElementsByTagName("seriesid"):
            messages.error(request, "No TV Series was found with %s!" % params)
            return HttpResponseRedirect('/distracted/search/')
        #    parse results
        seriesId    = xmldom.getElementsByTagName("seriesid")[0].firstChild.nodeValue
        seriesName  = xmldom.getElementsByTagName("SeriesName")[0].firstChild.nodeValue
        seriesAired = xmldom.getElementsByTagName("FirstAired")[0].firstChild.nodeValue
        seriesOverview = xmldom.getElementsByTagName("Overview")[0].firstChild.nodeValue
        #    create context and render result
        return render(request, 'distracted/searchResult.html',
            {'seriesId'         : seriesId,
             'seriesName'       : seriesName,
             'seriesOverview'   : seriesOverview,
             'seriesAired'      : seriesAired})
    else:
        messages.error(request, "You submitted an empty form!")
        return HttpResponseRedirect('/distracted/search/')
