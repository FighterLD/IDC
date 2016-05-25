from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', 'polls.views.index'),
]

if __name__ = '__main__':
    pass
