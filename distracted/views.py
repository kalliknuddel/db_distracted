from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404
from django.views import generic

from .models import Series


class IndexView(generic.ListView):
    template_name = 'distracted/index.html'
    context_object_name = 'series_list'

    def get_queryset(self):
        return Series.objects.order_by('name')

class DetailView (generic.DetailView):
    model = Series
    template_name = 'distracted/detail.html'
