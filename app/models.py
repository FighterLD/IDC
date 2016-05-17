# coding: utf-8
from __future__ import unicode_literals

import os

from django.db import models


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMDB.settings")

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)
SERVICE_TYPES = (
    ('moniter', u"Moniter"),
    ('lvs', u"LVS"),
    ('db', u"Database"),
    ('analysis', u"Analysis"),
    ('admin', u"Admin"),
    ('storge', u"Storge"),
    ('web', u"WEB"),
    ('email', u"Email"),
    ('mix', u"Mix"),
)


class IDC(models.Model):
    """
    互联网数据中心(Internet Data Center)
    """
    name = models.CharField(max_length=64, verbose_name='名字')
    description = models.TextField(verbose_name='描述')

    contact = models.CharField(max_length=32, verbose_name='联系方式')
    telphone = models.CharField(max_length=32, verbose_name='手机号')
    address = models.CharField(max_length=128, verbose_name='地址')
    customer_id = models.CharField(max_length=128, verbose_name='用户id')

    create_time = models.DateField(auto_now=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC数据中心"
        verbose_name_plural = verbose_name


class Host(models.Model):
    idc = models.ForeignKey(IDC, verbose_name='IDC机房', blank=True, null=True)
    name = models.CharField(max_length=64, verbose_name='机器名')
    nagios_name = models.CharField(u"Nagios Host ID", max_length=64, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP地址')
    internal_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')
    user = models.CharField(max_length=64, verbose_name='用户名', blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    ssh_port = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(choices=SERVER_STATUS, verbose_name='状态', blank=True, null=True)

    brand = models.CharField(max_length=64, choices=[(i, i) for i in (u"DELL", u"HP", u"Other")],
                             blank=True, null=True,
                             verbose_name='机器品牌')
    model = models.CharField(max_length=64)
    cpu = models.CharField(max_length=64, verbose_name='CPU类型')
    core_num = models.SmallIntegerField(
        verbose_name='CPU数量', choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)])
    hard_disk = models.IntegerField(verbose_name='硬盘大小')
    memory = models.IntegerField()

    system = models.CharField(u"System OS", max_length=32,
                              choices=[(i, i) for i in (u"CentOS", u"FreeBSD", u"Ubuntu")],
                              )
    system_version = models.CharField(max_length=32, verbose_name='系统版本')
    system_arch = models.CharField(max_length=32,
                                   verbose_name='系统架构',
                                   choices=[(i, i) for i in (u"x86_64", u"i386")])

    create_time = models.DateField(verbose_name='新增日期', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
    guarantee_date = models.DateField(verbose_name='保质日期', auto_now_add=True)
    service_type = models.CharField(max_length=32, choices=SERVICE_TYPES, verbose_name='服务类型')
    description = models.TextField(verbose_name='服务描述')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Host"
        verbose_name_plural = verbose_name


class MaintainLog(models.Model):
    host = models.ForeignKey(Host)
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()

    def __unicode__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type, self.hard_type)

    class Meta:
        verbose_name = u"Maintain Log"
        verbose_name_plural = verbose_name


class HostGroup(models.Model):

    name = models.CharField(max_length=32)
    description = models.TextField()
    hosts = models.ManyToManyField(
        Host, verbose_name=u'Hosts', blank=True, related_name='groups')

    class Meta:
        verbose_name = u"Host Group"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class AccessRecord(models.Model):
    date = models.DateField()
    user_count = models.IntegerField()
    view_count = models.IntegerField()

    class Meta:
        verbose_name = u"Access Record"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s Access Record" % self.date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    hosts = Host.objects.filter()
    print hosts[0]
