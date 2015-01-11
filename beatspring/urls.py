from django.conf.urls import patterns, include, url
from django.contrib import admin
from landing import views


urlpatterns = patterns('',
    url(r'^$', 'landing.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
)
