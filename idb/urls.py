from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

from tastypie.api import Api
from idb.resources import ImageResource, PlatformResource, DeveloperResource, GameResource

admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(ImageResource())
v1_api.register(PlatformResource())
v1_api.register(DeveloperResource())
v1_api.register(GameResource())

urlpatterns = patterns('',
    url(r'^$', 'idb.views.home', name='home'),
    url(r'^developer/', include(patterns('',
        url(r'^$', 'idb.views.developers', name='developers'),
        url(r'^(?P<developer_id>\d+)/$', 'idb.views.developer', name='developer'),
    ))),
    url(r'^platform/', include(patterns('',
        url(r'^$', 'idb.views.platforms', name='platforms'),
        url(r'^(?P<platform_id>\d+)/$', 'idb.views.platform', name='platform'),
    ))),
    url(r'^game/', include(patterns('',
        url(r'^$', 'idb.views.games', name='games'),
        url(r'^(?P<game_id>\d+)/$', 'idb.views.game', name='game'),
    ))),
    url(r'^search/', 'idb.views.search', name='search'),
    url(r'^dynamic/', TemplateView.as_view(template_name="dynamic.html")),
    url(r'^queries/','idb.views.queries', name="queries.html"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
