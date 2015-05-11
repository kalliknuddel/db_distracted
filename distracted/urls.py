from django.conf.urls import include, url

from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
               #    /distracted/
               url (r'^$', views.IndexView.as_view(), name = 'index'),
               
               #    /add/
               url (r'^search/$', views.SearchSeries, name = 'search'),
               url (r'^add/$', views.AddSeries, name = 'add'),
               
               #    /distracted/5/
               url (r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]