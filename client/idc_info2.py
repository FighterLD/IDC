# coding:utf-8
'''
Created on 2016年5月18日

@author: likaiguo
'''
from __future__ import print_function, unicode_literals

import json
import platform
import urllib
import psutil


def platform_info(name='likaiguo-mac-6', force_update=False):
    host = {'name': 'likaiguo_test'}
    host['core_num'] = psutil.cpu_count()
    host['cpu'] = platform.machine()
    uname_result = platform.uname()
    host['system'] = uname_result[0]
    host['system_version'] = uname_result[2]
    host['system_arch'] = uname_result[4]

    sdiskusage = psutil.disk_usage('/')
    host['hard_disk'] = sdiskusage.total * 1 / (1024**3)

    mem = psutil.virtual_memory()
    host['memory'] = mem.total * 1 / (1024**3)
    print(json.dumps(host, indent=4, ensure_ascii=False))
    data = urllib.urlencode(query=host)
    print(data)
    response = urllib.urlopen(url='http://127.0.0.1:8000/idc/add', data=data)
    print(response)

    return host


if __name__ == '__main__':

    platform_info(name='likaiguo-12232')
