from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/', include('allauth.urls')),
	url(r'^$', TemplateView.as_view(template_name="index.html")),#'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),#'django.views.generic.simple.direct_to_template', {'template': 'profile.html' }),
    # Examples:
    # url(r'^$', 'Event4u.views.home', name='home'),
    # url(r'^Event4u/', include('Event4u.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
