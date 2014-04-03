from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

from tastypie.api import Api
from idb.resources import PlatformResource, DeveloperResource, GameResource

admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(PlatformResource())
v1_api.register(DeveloperResource())
v1_api.register(GameResource())

urlpatterns = patterns('',
    url(r'^$', 'idb.views.home', name='home'),
    url(r'^game/(?P<game_title>[\w|\W]+)/$', 'idb.views.game', name='game'),
    url(r'^platform/(?P<platform_name>[\w|\W]+)/$', 'idb.views.platform', name='platform'),
    url(r'^developer/(?P<developer_name>[\w|\W]+)/$', 'idb.views.developer', name='developer'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
