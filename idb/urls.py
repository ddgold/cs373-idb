from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'idb.views.home', name='home'),
    url(r'^game/(?P<game_id>\d+)/$', 'idb.views.game', name='game'),
    url(r'^platform/(?P<platform_id>\d+)/$', 'idb.views.platform', name='platform'),
    url(r'^developer/(?P<developer_id>\d+)/$', 'idb.views.developer', name='developer'),
    url(r'^admin/', include(admin.site.urls)),
)
