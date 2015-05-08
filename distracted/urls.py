from django.conf.urls import include, url

from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
               #    /distracted/
               url (r'^$', views.index, name = 'index'),
               
               #    /distracted/5/
               url (r'^(?P<series_id>[0-9]+)/$', views.detail, name='detail')
]