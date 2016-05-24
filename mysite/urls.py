from django.conf.urls import include,url

from django.contrib import admin

from polls

urlpatterns = [
#    url(r'^$', polls.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'polls.view.index'),
    url(r'^$/', 'polls.view.index'),
    url(r'^api/add/', 'polls.views.add_question'),
]
