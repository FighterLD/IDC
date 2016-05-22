# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('user_count', models.IntegerField()),
                ('view_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Access Record',
                'verbose_name_plural': 'Access Record',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u673a\u5668\u540d')),
                ('nagios_name', models.CharField(max_length=64, null=True, verbose_name='Nagios Host ID', blank=True)),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP\u5730\u5740', blank=True)),
                ('internal_ip', models.GenericIPAddressField(null=True, verbose_name='\u5185\u7f51IP', blank=True)),
                ('user', models.CharField(max_length=64, null=True, verbose_name='\u7528\u6237\u540d', blank=True)),
                ('password', models.CharField(max_length=128, null=True, blank=True)),
                ('ssh_port', models.IntegerField(null=True, blank=True)),
                ('status', models.SmallIntegerField(blank=True, null=True, verbose_name='\u72b6\u6001', choices=[(0, 'Normal'), (1, 'Down'), (2, 'No Connect'), (3, 'Error')])),
                ('brand', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u673a\u5668\u54c1\u724c', choices=[('DELL', 'DELL'), ('HP', 'HP'), ('Other', 'Other')])),
                ('model', models.CharField(max_length=64)),
                ('cpu', models.CharField(max_length=64, verbose_name='CPU\u7c7b\u578b')),
                ('core_num', models.SmallIntegerField(verbose_name='CPU\u6570\u91cf', choices=[(2, '2 Cores'), (4, '4 Cores'), (6, '6 Cores'), (8, '8 Cores'), (10, '10 Cores'), (12, '12 Cores'), (14, '14 Cores'), (16, '16 Cores'), (18, '18 Cores'), (20, '20 Cores'), (22, '22 Cores'), (24, '24 Cores'), (26, '26 Cores'), (28, '28 Cores')])),
                ('hard_disk', models.IntegerField(verbose_name='\u786c\u76d8\u5927\u5c0f')),
                ('memory', models.IntegerField()),
                ('system', models.CharField(max_length=32, verbose_name='System OS', choices=[('CentOS', 'CentOS'), ('FreeBSD', 'FreeBSD'), ('Ubuntu', 'Ubuntu')])),
                ('system_version', models.CharField(max_length=32, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('system_arch', models.CharField(max_length=32, verbose_name='\u7cfb\u7edf\u67b6\u6784', choices=[('x86_64', 'x86_64'), ('i386', 'i386')])),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='\u65b0\u589e\u65e5\u671f')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('guarantee_date', models.DateField(auto_now_add=True, verbose_name='\u4fdd\u8d28\u65e5\u671f')),
                ('service_type', models.CharField(max_length=32, verbose_name='\u670d\u52a1\u7c7b\u578b', choices=[('moniter', 'Moniter'), ('lvs', 'LVS'), ('db', 'Database'), ('analysis', 'Analysis'), ('admin', 'Admin'), ('storge', 'Storge'), ('web', 'WEB'), ('email', 'Email'), ('mix', 'Mix')])),
                ('description', models.TextField(verbose_name='\u670d\u52a1\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': 'Host',
                'verbose_name_plural': 'Host',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('hosts', models.ManyToManyField(related_name='groups', verbose_name='Hosts', to='app.Host', blank=True)),
            ],
            options={
                'verbose_name': 'Host Group',
                'verbose_name_plural': 'Host Group',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u5b57')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('contact', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('telphone', models.CharField(max_length=32, verbose_name='\u624b\u673a\u53f7')),
                ('address', models.CharField(max_length=128, verbose_name='\u5730\u5740')),
                ('customer_id', models.CharField(max_length=128, verbose_name='\u7528\u6237id')),
                ('create_time', models.DateField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': 'IDC\u6570\u636e\u4e2d\u5fc3',
                'verbose_name_plural': 'IDC\u6570\u636e\u4e2d\u5fc3',
            },
        ),
        migrations.CreateModel(
            name='MaintainLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maintain_type', models.CharField(max_length=32)),
                ('hard_type', models.CharField(max_length=16)),
                ('time', models.DateTimeField()),
                ('operator', models.CharField(max_length=16)),
                ('note', models.TextField()),
                ('host', models.ForeignKey(to='app.Host')),
            ],
            options={
                'verbose_name': 'Maintain Log',
                'verbose_name_plural': 'Maintain Log',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(verbose_name='IDC\u673a\u623f', blank=True, to='app.IDC', null=True),
        ),
    ]
