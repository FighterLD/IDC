from django.conf.urls import include,url

from django.contrib import admin

import polls

urlpatterns = [
#    url(r'^$', polls.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/', 'polls.views.index'),
    url(r'^$/', 'polls.views.index'),
    url(r'^api/add/', 'polls.views.add_question'),
]
