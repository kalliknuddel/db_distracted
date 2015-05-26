from django.conf.urls import include, url

from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
               #    /distracted/
               #    index list view
               url (r'^$', views.IndexView, name = 'realIndex'),

               url (r'^list/$',             views.SeriesList.as_view(),     name = 'index'),
               url (r'^list/banners/$',             views.SeriesListBanners.as_view(),     name = 'indexBanners'),

               #    search stuff
               url (r'^search/$',           views.SearchSeries,             name = 'search'),
               url (r'^result/$',           views.SearchResult.as_view(),   name = 'searchResult'),
               url (r'^result/(?P<seriesid>[0-9]+)/$',      views.SearchDetail.as_view(),   name = 'searchDetail'),
               url (r'^result/(?P<seriesid>[0-9]+)/save/$', views.SearchSave.as_view(),     name = 'searchSave'),

               #    /distracted/5/
               #    detailed view
               url (r'^(?P<pk>[0-9]+)/$', views.SeriesDetail.as_view(), name='detail'),
               url (r'^(?P<pk>[0-9]+)/delete/$', views.SeriesDelete.as_view(), name='delete'),
               
               #    django's auth model
               url('^', include('django.contrib.auth.urls')),

]
