from django.conf.urls import patterns, include, url
from sources.models import Source

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whatShallIWear.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^outfits/', include('outfits.urls', namespace='outfits')),
    )