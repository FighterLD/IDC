import xadmin
from xadmin.plugins import xversion

from django.conf.urls import patterns, include, url
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
xversion.register_models()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^idc/', include('app.urls')),
    url(r'^$', 'app.views.index'),
)
