from django.conf.urls import patterns, include, url
# for custom views handling

from manager.views import EventCreate

from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/', include('allauth.urls')),
	url(r'^$', TemplateView.as_view(template_name="index.html")),#'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^todo/$','manager.views.todo'),

    url(r'^create/$','manager.views.EventCreate', name='event_add'),
    url(r'^events/(?P<event_id>\d+)/$','manager.views.addTeam', name='team_add'),
    url(r'^view/(?P<event_id>\d+)/$','manager.views.eventView', name='view_events'),
    # url(r'^create/add_team$','manager.views.addTeam',{'event_add': 3} name='add_team'),
    # *************edited*************
    # url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),#'django.views.generic.simple.direct_to_template', {'template': 'profile.html' }),
    # url(r'manage/create/$', 'manager.views.EventCreate', name='event_add'),
    # ***********edited****************
    # Examples:
    # url(r'^$', 'Event4u.views.home', name='home'),
    # url(r'^Event4u/', include('Event4u.foo.urls')),
    url(r'^accounts/profile/$','manager.views.showProfile', name='my_profile'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
