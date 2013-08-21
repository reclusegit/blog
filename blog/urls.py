from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'record.views.index'),
    url(r'^login/$', 'record.views.login'),
    url(r'^logout/$', 'record.views.logout'),
    url(r'^regist/$', 'record.views.regist'),
    url(r'^search-form/$', 'record.views.search_form'),
    url(r'^search/$', 'record.views.search'),
)
