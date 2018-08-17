# Django-Blog
基于 Django 框架的简易个人博客。


---

## 简介

关于博客这件事，基于 jekyll 和 hexo 的博客都试过，csdn 和博客园和 segment fault 都写过，总不能觉得满意…… 最后还是决定自己造一个了_(:з)∠)_

预览网址： http://codingcat.cn

## 相关技术

当前版本： v 0.1

基于 Django 搭建而成
- 前端页面：样式基于 Bootstrap 4
- 管理后台：直接用了 Django 自带的 Admin
- Markdown：使用 Editor.md （待添加）
- 数据库：基于 Mysql
- 搜索：基于 haystack 和 whoosh （待添加）
- 标签文字云：JQCloud

项目不断更新完善中。欢迎 star、fork 和 PR。

## 本地部署流程

#### 安装依赖
项目基于 Python 3，需要在项目根目录下运行
```commandline
pip3 install -r requirements.txt
```

#### 修改数据库
在 DjangoBlog/settings.py 中，找到 DATABASES 部分，修改为你自己的 mysql 数据库位置和账户。


#### 数据库建表
在项目根目录下运行
```commandline
python3 manage.py makemigrations
python3 manage.py migrate
```

#### 创建管理员账号
在项目根目录下运行
```commandline
python3 manage.py createsuperuser
```
然后按照提示，设置管理员的用户名密码即可。

#### 本地运行
在项目根目录下运行
```commandline
python3 manage.py runserver 8888
```
可修改为其他端口。

运行后在浏览器访问 http://127.0.0.1:8888 即可看到站点。

访问 http://127.0.0.1:8888/manager 查看管理后台。



## 个性化定制
可根据你的需要修改项目中的内容。（这部分说明，后续再详细补充）

## 更新日志
v0.1 2018/08/12 搭建原始框架