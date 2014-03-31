from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'idb.views.home', name='home'),
    url(r'^games/(?P<game_id>\d+)/$', 'idb.views.game', name='game'),
    url(r'^admin/', include(admin.site.urls)),
)
