""" 为应用程序users定义URL模式 """

from django.urls import path, include
# from django.contrib.auth import login 原书代码
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users'
LoginView.template_name = 'user/login.html'
urlpatterns = [
    # 登录页面
    # url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login 原书代码'), 
    path('login/', LoginView.as_view(), name='login')
]
