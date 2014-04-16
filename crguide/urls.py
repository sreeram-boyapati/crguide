from django.conf.urls import patterns, include, url
from django.contrib import admin
import offices.urls as offices_urls
import questions.urls as questions_urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crguide.views.home', name='home'),
    # url(r'^crguide/', include('crguide.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += offices_urls.urlpatterns
urlpatterns += questions_urls.urlpatterns