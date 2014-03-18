from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'idb.views.home', name='home'),
    url(r'^wii_u',
        TemplateView.as_view(template_name='wii_u.html'),
        name='wii_u'),
    url(r'^call_of_duty_4',
        TemplateView.as_view(template_name='call_of_duty_4.html'),
        name='call_of_duty_4'),
    url(r'^cing',
        TemplateView.as_view(template_name='cing.html'),
        name='cing'),
    url(r'^hotel_dusk',
        TemplateView.as_view(template_name='hotel_dusk.html'),
        name='hotel_dusk'),
    url(r'^infinity_ward',
        TemplateView.as_view(template_name='infinity_ward.html'),
        name='infinity_ward'),
    url(r'^nintendo_ds',
        TemplateView.as_view(template_name='nintendo_ds.html'),
        name='nintendo_ds'),
    url(r'^platinum_games',
        TemplateView.as_view(template_name='platinum_games.html'),
        name='platinum_games'),
    url(r'^the_wonderful_101',
        TemplateView.as_view(template_name='the_wonderful_101.html'),
        name='the_wonderful_101'),
    url(r'^xbox_360',
        TemplateView.as_view(template_name='xbox_360.html'),
        name='xbox_360'),
    url(r'^admin/', include(admin.site.urls)),
)
