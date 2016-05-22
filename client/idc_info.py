# coding:utf-8
'''
Created on 2016年5月18日

@author: likaiguo
'''
import platform
import psutil

from app.models import Host


def platform_info(name='likaiguo-mac-6', force_update=False):
    host = Host.objects.filter(name=name).first()
    if not host or force_update:
        if not host:
            host = Host(name=name)
        host.core_num = psutil.cpu_count()
        host.cpu = platform.machine()
        uname_result = platform.uname()
        host.system = uname_result[0]
        host.system_version = uname_result[2]
        host.system_arch = uname_result[4]

        sdiskusage = psutil.disk_usage('/')
        host.hard_disk = sdiskusage.total * 1.0 / (1024**3)

        mem = psutil.virtual_memory()
        host.memory = mem.total * 1.0 / (1024**3)
        host.save()


if __name__ == '__main__':

    platform_info(name='likaiguo-12232')
