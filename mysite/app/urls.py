from django.urls import path
from django.views.generic.base import View
#from .views import index_html, Index
from .views import Index
from .views import Message, Regiser
# urlpatterns = [
#     # path('', index),
#     path('index/', index_html),
#     # 第一种
#     # path("<str:name>", Index.as_view()),
#     # 第二种
#     path("<str:name>", Index.as_view())
# ]

urlpatterns = [
    path('', Index.as_view()),
    path('message/<str:message_type>', Message.as_view()),
    path('', Regiser.as_view(), name='regiser')
]
