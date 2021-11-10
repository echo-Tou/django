from django.urls import path
from django.urls.conf import include
from .views import index, cart

urlpatterns = [
  path('', index.index, name='index'),


  path('login/', index.login, name="web_login"),
  path('dologin', index.dologin, name="web_dologin"),
  path('loginout', index.loginout, name="web_loginout"),
  path('verify', index.verify, name="web_verify"), #验证码

  #为url路由添加请求前缀web/,凡是带此前缀的url地址必须登录后才可以访问
  path('web/', include([
    path('', index.webindex, name='web_index'),

    # 购物车信息管理路由
    path('cart/add/<str:pid>',cart.add, name='web_cart_add'),
    

  ]))
]
