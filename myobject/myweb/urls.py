from django.urls import path
from django.urls.conf import include
from .views import index, cart, orders

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
    path('cart/delete/<str:pid>',cart.delete, name='web_cart_delete'),
    path('cart/clear',cart.clear, name='web_cart_clear'),
    path('cart/change',cart.change, name='web_cart_change'),

    # 订单信息管理路由
    path('orders/<int:pIndex>',orders.index, name='web_orders_index'),

    # web_orders_insert
    path('orders/<int:pIndex>', orders.index, name="web_orders_index"), #浏览订单
    path('orders/insert',orders.insert, name='web_orders_insert'),
    path('orders/detail',orders.detail, name='web_orders_detail'),
    path('orders/status',orders.status, name='web_orders_status'),
    

  ]))
]
