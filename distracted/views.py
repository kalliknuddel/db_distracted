from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView

import urllib

from .models import Series
from .forms import SearchSeriesForm


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

def AddSeries (request):
    if 'seriesName' in request.POST:
        message = 'You searched for: %r' % request.POST['seriesName']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
        
