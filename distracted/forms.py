
from django import forms
from django.forms.models import ModelForm

from .models import Series


class SearchSeriesForm (forms.Form): 
    name = forms.CharField()

"""
class AddSeriesForm (ModelForm):
    class Meta:
        model = Series
        fields = ['series_id', 
                  'name',
                  'alias',
                  'overview',
                  'banner',
                  'first_aired']
"""
