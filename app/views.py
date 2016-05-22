# coding:utf-8
'''
Created on 2016年5月19日

@author: likaiguo
'''
from django.http import HttpResponse, JsonResponse
from app.models import Host


def index(request):

    return HttpResponse('hello world ')


def add_host(request):
    request_dict = request.GET
    name = request_dict.get('name')
    force_update = request_dict.get('force_update')
    print request_dict
    data = {k: v for k, v in request_dict.items()}

    host = Host.objects.filter(name=name).first()
    if not host or force_update:
        if not host:
            host = Host(**data)

        host.save(force_insert=True)

    data = {
        'msg': 'ok',
        'status': 'ok'
    }

    return JsonResponse(data)

if __name__ == '__main__':
    pass
