# 渲染页面
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .consts import MessageType
from .forms import Auth
from .models import Users
# Create your views here.

# def index(request):
#     return  HttpResponse('hello world')

# def index_html(request):
#     return HttpResponse('hello django')

# class Index(View):
#     # 第一种方法(建议使用第一种)
#     # def get(self, request, name):
#     #     return render(request, 'index.html', {'name': name})
#     # 第二种方法
#     # def get(self, request):
#     #     name = request.GET.get('name', '')
#     #     return render(request, 'index.html', {'name': name})
#     def get(self, request, name):
#         list_data = range(10)
#         return render(request, 'index.html', {'name': name, 'list_data': list_data})

class Index(View):
    def get(self, request):
        ob = Users()
        print(ob.age)
        ob.name = '张三'
        ob.age = 20
        ob.phone = '1234456'
        ob.save()

        # data = {}
        # data['count'] = 20
        # return render(request, 'index2.html', data)
        return HttpResponse('AAA')

class Message(View):
    def get(self, request, message_type):
        data = {}
        try:
            message_type_obj = MessageType[message_type]
            print(message_type_obj)
        except:
            data['error'] = '没有这个消息类型'
            return render(request, 'message.html', data)
        
        message = request.GET.get('message', '')
        print('message:', message)
        if not message:
            data['error'] = '消息类型不能为空'
            return render(request, 'messages.html', data)
        
        data['message'] = message
        data['message_type'] = message_type_obj    # message_type == MessageType.info 或者 MessageType.warning/error/danger
        return render(request, 'message.html', data)

class Regiser(View):
    def get(self, request):
        form = Auth()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        form = Auth(request.POST)
        print('form', form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            return HttpResponse('username: {}, password: {}'.format(username, password))
        return HttpResponse('ERROR')