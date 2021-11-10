from django.urls import path
from .views import  index_user
from . import views
from . import views_image
urlpatterns = [
    #path('edit/', index, name='index'),
    path('',index_user, name='index_user'),
    # 配置users信息操作路由
    path('users', views.indexUsers, name='indexusers'),
    path('users/add', views.addUsers, name='adduser'),
    path('users/insert', views.insertUsers, name='insertusers'),
    path('users/del/<int:uid>', views.delUsers, name='delusers'),
    path('users/edit/<int:uid>', views.editUsers, name='editusers'),
    path('users/update', views.updateUsers, name='updateusers'),
    path('templates_demo', views.templates_demo, name='templates_demo'),
    path('demo', views.demo, name='demo'),
    # 文件上传路由配置
    path('upload', views.upload, name='upload'),   #加载文件上传表单页
    path('doupload', views.doupload, name='doupload'),

    # 分页浏览用户信息
    path('pageusers/<int:pIndex>', views.pageUsers, name='pageusers'),

    #
    path('image', views_image.indexImages, name='indeximage'),
    path('image/addimage', views_image.addimage, name='addimage'),
    path('image/insertimage', views_image.insertimage, name='insertimage'),
    path('image/editimage/<int:uid>', views_image.editimage, name='editimage'),
    path('image/updateimage', views_image.updateimage, name='updateimage'),
    path('image/delimage/<int:uid>', views_image.delimage, name='delimage'),
]