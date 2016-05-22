# coding:utf-8
'''
Created on 2016年5月21日

@author: likaiguo
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url('add', views.add_host),
]

if __name__ == '__main__':
    pass
