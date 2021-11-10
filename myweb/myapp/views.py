from django import http
from django.conf import urls
from django.conf.urls import handler404
from django.db import models
from django.db.models import aggregates
from django.shortcuts import render
from django.http import HttpResponse, Http404, response
from django.urls import reverse
from django.shortcuts import redirect

from .models import Users
from PIL import Image
from django.core.paginator import Paginator
# Create your views here.

# def index(request):
#     print(reverse('index'))   # 通过路由反向生成url地址
#     # return redirect(reverse('index'))  # 执行浏览器重定向
#     return HttpResponse('hello world!')


def index_user(request):
    # 执行model操作
    # 添加操作
        # ob = Users()
        # print(ob.age)
        # ob.name = '张三'
        # ob.age = 20
        # ob.phone = '1234456'
        # ob.save()

    # 删除操作
    # mod = Users.objects  #获取users的model对象
    # user = mod.get(id=1) #获取id=1的数据信息
    # print(user.name)
    # user.delete()  # 删除

    # 修改操作
    # ob = Users.objects.get(id=2)
    # ob.name = 'TT'
    # ob.age = '18'
    # ob.save()

    # 查
    mod = Users.objects
    ulist = mod.all()  #获取所有数据
    ulist = mod.filter(name='小刘')
    ulist = mod.filter(age__gt=20) # 获取所有age大于20的
    ulist = mod.filter(age__gte=20) # 获取所有age大于等于20的
    ulist = mod.filter(age__lte=20)
    ulist = mod.order_by('age') # 按age升序排序
    ulist = mod.order_by('age')[:3]  # 按age升序排序 只获取前三条
    for m in ulist:
        print(m)


    #return HttpResponse("首页 <br/> <a href='/users'>用户信息管理</a> <br/> <a href='/upload'>文件上传案例</a>")
    return render(request, 'myapp/users/index_user.html')

# 加载文件上传表单
def upload(request):
    return render(request, 'myapp/upload.html')

# 执行文件上传处理
def doupload(request):
    myfile = request.FILES.get('pic', None)
    if not myfile:
        return HttpResponse('没有上传文件')
    destination = open('./static/pic/' + str(myfile), 'wb+')
    for chunk in myfile.chunks():  #分块写入文件
        destination.write(chunk)
    destination.close()
    # print(myfile)
    # print(request.POST.get('title'))

    # 执行图片缩放
    im = Image.open("./static/pics/"+ myfile)
    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((75, 75))
    # 把缩放后的图像用jpeg格式保存: 
    im.save("./static/pics/s_"+myfile, None)

    #执行图片删除
    #os.remove("./static/pics/"+filename)

    return HttpResponse('上传的文件', myfile)


# 浏览用户信息
def indexUsers(request):
    try:
        ulist = Users.objects.all()
        context = {'userslist': ulist}
        return render(request, 'myapp/users/index.html', context)
    except:
        return HttpResponse('没有用户信息')

# 分页浏览用户信息
def pageUsers(request, pIndex=1):
    try:
        #kw = request.GET.get('keyword', None)
        kw = request.GET.get('keyword', '')
        mywhere = ''
        if kw:
            ulist = Users.objects.filter(name__contains=kw)  # 对name字段做包含式查询 也可以说是模糊查询
            mywhere = '?keyword={}'.format(kw)
        else:
            ulist = Users.objects.filter()
        p = Paginator(ulist,5)   # 以5条数据一页实例化分页对象
        # ulist = p.page(1)
        if pIndex < 1:
            pIndex = 1
        if pIndex > p.num_pages:
            pIndex = p.num_pages

        ulist = p.page(pIndex)
        context = {'userslist': ulist,'pIndex': pIndex, 'pagelist': p.page_range, 'pagecount': p.num_pages, 'mywhere': mywhere, 'kw': kw}
        return render(request, 'myapp/users/index_page.html', context)
    except:
        return HttpResponse('没有用户信息')

# 加载添加用户信息表单
def addUsers(request):
    return render(request, 'myapp/users/add.html')
    
# 执行用户信息添加
def insertUsers(request):
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info': '添加成功'}
    except:
        context = {'info': '添加失败'}
    return render(request, 'myapp/users/info.html', context)

# 执行用户信息删除
def delUsers(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info': '删除失败'}
    return render(request, 'myapp/users/info.html', context)

# 加载用户信息修改表单
def editUsers(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)
        context = {'user': ob}
        return render(request, 'myapp/users/edit.html', context)
    except:
        context = {'info': '没有找到要修改的数据'}
    return render(request, 'myapp/users/edit.html', context)

# 执行用户信息修改
def updateUsers(request):
    try:
        uid =  request.POST['id']   # 获取要修改数据的id
        print(uid)
        ob = Users.objects.get(id=uid)  # 根据id查询要修改的数据
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info': '添加成功'}
    except:
        context = {'info': '添加失败'}
    return render(request, 'myapp/users/info.html', context)

def templates_demo(request):
    return render(request, 'myapp/index.html')

def demo(request):
    '''模板继承'''
    return render(request, 'myapp/demo.html')