from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'db_distracted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #    django's auth model
    #url('^', include('django.contrib.auth.urls')),

    url(r'^distracted/', include('distracted.urls', namespace="distracted")),
    url(r'^admin/', include(admin.site.urls)),
)

#^login/$ [name='login']
#^logout/$ [name='logout']
#^password_change/$ [name='password_change']
#^password_change/done/$ [name='password_change_done']
#^password_reset/$ [name='password_reset']
#^password_reset/done/$ [name='password_reset_done']
#^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
#^reset/done/$ [name='password_reset_complete']
#
