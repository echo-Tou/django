from django import http
from django.conf import urls
from django.conf.urls import handler404
from django.db import models
from django.db.models import aggregates
from django.shortcuts import render
from django.http import HttpResponse, Http404, response
from django.urls import reverse
from django.shortcuts import redirect

from .models import Images
from PIL import Image
from django.core.paginator import Paginator


# 浏览相册信息
def indexImages(request):
    try:
        ulist = Images.objects.all()
        context = {'userslist': ulist}
        return render(request, 'myapp/images/index.html', context)
    except:
        return HttpResponse('没有相册信息')

#添加相册信息
def addimage(request):
    return render(request, 'myapp/images/add.html')

#插入相册信息
def insertimage(request):
    try:
        ob = Images()
        myfile = request.FILES.get('image', None)
        if not myfile:
            return HttpResponse('没有上传文件')
        destination = open('./static/pic/' + str(myfile), 'wb+')
        for chunk in myfile.chunks():  #分块写入文件
            destination.write(chunk)
        destination.close()
        ob.name = request.POST['name']
        ob.image = myfile
        ob.save()
        context = {'info': '添加成功'}
    except:
        context = {'info': '添加失败'}
    return render(request, 'myapp/images/info.html', context)
    
# 修改相册信息
def editimage(request, uid=1):
    ob = Images.objects.get(id=uid)
    context = {'image': ob}
    return render(request, 'myapp/images/edit.html', context)

def updateimage(request):
    try:
        uid = request.POST['id']
        print(uid)
        ob = Images.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.image = request.POST['image']
        ob.save()
        context = {'info': '修改成功'}
    except:
        context = {'info': '修改失败'}
    return render(request, 'myapp/images/info.html', context)

# 删除相册信息
def delimage(request, uid=1):
    ob = Images.objects.get(id=uid)
    ob.delete()
    context = {'info': '删除成功'}
    return render(request, 'myapp/images/info.html', context)

# 执行文件上传处理
def doupload(request):
    myfile = request.FILES.get('image', None)
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