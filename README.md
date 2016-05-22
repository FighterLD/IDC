# CMDB(configuration management database)
好玩IDC资产管理系统

[资产管理系统Cmdb助力自动化运维实施](http://os.51cto.com/art/201403/431788.htm)
##项目说明


## 运行部署

### 服务端

```
mkvirtualenv IDC
pip install -r requirements.txt
python manage.py runserver
```
然后打开浏览器

账号密码: likaiguo 123456

### 客户端



## 用Django进行mysql类数据库变更方法(migrate)

##常见问题

### 1.mysql包安装不了

mac和Ubuntu的装法不一样,一定记得Google一下,不要愣住了

### 2.xadmin没有安装好

如果使用 pip install -r requirements.txt 发现没有安装好xadmin  

```
pip install -e git+https://github.com/likaiguo/django-xadmin.git@9dab6a897e0e65cf7b50763c2f6f9b1a5bb0165e#egg=django_xadmin
```
重新安装一下