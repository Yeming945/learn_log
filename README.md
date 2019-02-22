## 18 Django入门
### 18.1 建立项目
#### 18.1.5 安装 Django 
pip install Django
#### 18.1.6 Django 中创建项目
django-admin.py startproject learning_log .
#### 18.1.7 创建数据库
python manage.py migrate
#### 18.1.8 查看项目
python mange.py runserver
### 18.2 创建应用程序
python manage.py startapp learning_logs
#### 18.2.2 激活模型
python manage.py makemigrations learning_logs
python manage.py migrate
#### 18.2.3 Django管理网站
1. 创建超级用户
python manage.py createsuperuser
user:admin
password:123456
2. 向管理网站注册模型
详见admin.py文件
3. 添加主题
#### 18.2.4 定义模型 Entry
``` python
# learning_logs\models.py修改代码
# 原书代码
topic = models.ForeignKey(Topic)
# 修改后
topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
```
#### 18.2.5 迁移模型 Entry
python manage.py makemigrations learning_logs
python manage.py migrate
#### 18.2.6 向管理网站注册 Entry

### 18.3 创建网页：学习笔记主页
#### 18.3.1 映射 URL
``` python
# learning_log\urls.py修改代码
# 原书代码
from django.conf.urls import include, url
from django.contrib import admin
    urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
] 
# 改为
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls', namespace='learning_logs')),
]
# learning_logs\urls.py修改代码
 """定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views
urlpatterns = [
# 主页
    url(r'^$', views.index, name='index'),
] 
# 修改为
from django.urls import path
from . import views
app_name = 'learning_logs' # 增加app_name
urlpatterns = [
    # 主页
    path('', views.index, name='index'),    # 主页
]
```
### 18.4 创建其他网页
#### 18.4.2 显示所有主题的页面
1. URL模式
``` python
# learning_logs\urls.py 修改代码
# 原书代码
# 显示所有的主题
url(r'^topics/$', views.topics, name='topics')
# 修改为
path('topics/', views.topics, name='topics')
```
#### 18.4.3 显示特定主题的页面
``` python
# learning_logs\urls.py 修改代码
# 原书代码
# 显示所有的主题
url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
# 修改为
path('topics/<topic_id>/', views.topic, name='topic')

```
## 19 用户账户
### 19.1 让用户能够输入数据
``` python
# learning_logs\views.py 修改代码
# 原书代码
from django.core.urlresolvers import reverse 
# 修改为
from django.urls import reverse
```

#### 19.1.2 添加新条目
``` python
# learning_logs\urls.py 修改代码
# 原书代码
url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry')
# 修改为
path('new_topic/', views.new_topic, name='new_topic')
```
#### 19.1.3 编辑条目
``` python
# learning_logs\urls.py 修改代码
url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry')
```
#### 19.2.2 登录页面
``` python
# users\urls.py 修改代码
"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name':'users/login.html'} name='login'),
] 
# 修改为
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
LoginView.template_name = 'user/login.html'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]
```
#### 19.2.3 注销
``` python
# users\urls.py 修改代码
url(r'^logout/$', views.logout_view, name='logout'), 
# 修改为
path('logout/', views.logout_view, name='logout'),
# users\views.py 修改代码
from django.core.urlresolvers import reverse
# 修改为
from django.urls import reverse
```

#### 19.2.4 注册页面
``` python 
# urls.py 
url(r'^register/$', views.register, name='register')
# after
path('register/', views.register, name='register')
# views.py
from django.core.urlresolvers import reverse
after
from django.urls import reverse

```
### 19.3 让用户拥有自己的数据
#### 19.3.2 将数据关联到用户
``` python
# models.py 
owner = models.ForeignKey(User)
# after
owner = models.ForeignKey(User, on_delete=models.CASCADE)

```