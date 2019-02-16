### 18.1 建立项目
##### 18.1.5 安装 Django 
pip install Django
##### 18.1.6 Django 中创建项目
django-admin.py startproject learning_log .
##### 18.1.7 创建数据库
python manage.py migrate
##### 18.1.8 查看项目
python mange.py runserver

### 18.2 创建应用程序
python manage.py startapp learning_logs
##### 18.2.2 激活模型
python manage.py makemigrations learning_logs
python manage.py migrate

##### 18.2.3 Django管理网站
1. 创建超级用户
python manage.py createsuperuser
user:admin
password:123456
2. 向管理网站注册模型
详见admin.py文件
3. 添加主题
##### 18.2.4 定义模型 Entry
详见model.py文件
##### 18.2.5 迁移模型 Entry
python manage.py makemigrations learning_logs
python manage.py migrate
##### 18.2.6 向管理网站注册 Entry
