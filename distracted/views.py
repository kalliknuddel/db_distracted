from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404

from .models import Series


def index(request):
    series_list = Series.objects.order_by('name')
    context = {'series_list' : series_list}
    return render(request, 'distracted/index.html', context)

def detail (request, series_id):
    series = get_object_or_404(Series, id=series_id)
    context = { 'series' : series }
    return render (request, 'distracted/detail.html', context)
