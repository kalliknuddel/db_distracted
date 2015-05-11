from django.conf.urls import include, url

from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
               #    /distracted/
               #    index list view
               url (r'^$', views.IndexView.as_view(), name = 'index'),

               #    search stuff
               url (r'^search/$',           views.SearchSeries              , name = 'search'),
               url (r'^result/$',           views.SearchResult.as_view()    , name = 'searchResult'),
               url (r'^result/(?P<seriesid>[0-9]+)/$',  views.SearchDetail.as_view()    , name = 'searchDetail'),

               #    /distracted/5/
               #    detailed view
               url (r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]
