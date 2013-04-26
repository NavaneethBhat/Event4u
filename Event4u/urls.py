from django.conf.urls import patterns, include, url
# for custom views handling

from manager.views import EventCreate

from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/', include('allauth.urls')),
	url(r'^$', TemplateView.as_view(template_name="index.html")),#'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^events/todo/(?P<team_id>\d+)$','manager.views.todo'),

    url(r'^create/$','manager.views.EventCreate', name='event_add'),
    url(r'^events/add/(?P<event_id>\d+)/$','manager.views.addTeam', name='team_add'),
    url(r'^view/(?P<event_id>\d+)/$','manager.views.eventView', name='view_events'),
    # url(r'^events/tasks/(?P<team_id>\d+)$','manager.views.addTask', name='view_events'),
    url(r'^view/teams/(?P<event_id>\d+)/$','manager.views.view_teams', name='view_teams'),
    # url(r'^create/add_team$','manager.views.addTeam',{'event_add': 3} name='add_team'),
    # Examples:
    # url(r'^$', 'Event4u.views.home', name='home'),
    # url(r'^Event4u/', include('Event4u.foo.urls')),
    url(r'^accounts/profile/$','manager.views.showProfile', name='my_profile'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$','manager.views.logout_view', name='my_profile'),

)
