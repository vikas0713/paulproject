from django.conf.urls import include, url
from django.contrib import admin
from views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^accounts/login', login, name='login'),
    url(r'^validate/', validate),
    url(r'^accounts/logout', logout , name='logout'),
    url(r'get_status/(?P<status>\w+)/$', status),
    url(r'load_get/(?P<load>\d+)/$', get_load),
    url(r'add_load/',add_load),
    url(r'add_driver/',add_driver),
    url(r'all/',all_records),
    url(r'update_status/(?P<id>\d+)/$', update_status),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()