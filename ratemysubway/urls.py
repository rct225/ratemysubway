from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ratemysubway.views.home', name='home'),
    # url(r'^ratemysubway/', include('ratemysubway.foo.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^subwayrating/$', 'subwayrating.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subwayrating/(?P<slug>[^\.]+).html', 'subwayrating.views.view_comment', name='view_comment'),
)
