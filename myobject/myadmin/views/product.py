from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Shop, User, Category, Product
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import random, os
import hashlib
import time



# Create your views here.

def index(request, pIndex=1):
    '''浏览信息'''
    smod = Product.objects
    slist = smod.filter(status__lt=9)
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = slist.filter(name__contains=kw)
        mywhere.append('keyword='+kw)
    cid = request.GET.get("category_id", '')
    if cid:
        print('cid',cid)
        slist = slist.filter(category_id=cid)
        mywhere.append('category_id='+str(slist))
     
    slist = slist.order_by('id') # 对id进行排序

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist,5) # 以每页5条数据分页
    print(page)
    maxpage = page.num_pages  # 获取最大页数
    if pIndex > maxpage:
        pIndex = maxpage
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  #获取当前页数据
    plist = page.page_range #获取页面列表信息

    for vo in list2:
        sob = Shop.objects.get(id=vo.shop_id)
        cob = Category.objects.get(id=vo.category_id)
        vo.shopname = sob.name
        vo.category = cob.name

    context = {'productlist': list2, 'plist': plist, 'pIndex': pIndex, 'maxpage':maxpage, 'mywhere':mywhere}
    return render(request, 'myadmin/product/index.html', context)

def add(request):
    '''
    加载信息添加表单
    ''' 
    # 获取当前所有店铺
    slist = Shop.objects.values('id','name')
    # print('slist', slist)
    context = {'shoplist': slist}
    return render(request, 'myadmin/product/add.html', context)

def insert(request):
    '''
    执行信息添加
    '''
    try:
        # 菜品图片处理
        myfile = request.FILES.get("cover_pic",None)
        if not myfile:
            return HttpResponse("没有菜品图片上传文件信息")
        cover_pic = str(time.time())+"."+myfile.name.split('.').pop()
        destination = open("./static/uploads/product/"+cover_pic,"wb+")
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()

        # 实例化model，封装信息，并执行添加
        ob = Product()
        ob.shop_id = request.POST.get('shop_id')
        print('category_id', ob.category_id)
        ob.category_id = request.POST.get('category_id')
        ob.cover_pic  = cover_pic
        ob.name = request.POST.get('name')
        ob.price = request.POST.get('price')
        ob.name = request.POST.get('name')
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '添加成功'}
    except Exception as err:
        print(err)
        context = {'info': '添加失败'}
    return render(request, 'myadmin/info.html', context)

def delete(request, pid=0):
    '''
    执行信息删除
    '''
    try:
        ob = Product.objects.get(id=pid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败'}
    return render(request, 'myadmin/info.html', context)
    #return JsonResponse(context)


def edit(request,pid=0):
    '''
    加载信息编辑表单
    '''
    try:
        ob = Product.objects.get(id=pid)
        context = {'product': ob}
        slist = Shop.objects.values('id','name')
        clist = Category.objects.values('id','name')
        context['shoplist'] = slist 
        return render(request, 'myadmin/product/edit.html', context)
    except Exception as err:
        print(err)
        context = {'info': '没有找到要修改的数据'} 
        return render(request, 'myadmin/info.html', context)

def update(request,pid=0):
    '''执行信息编辑'''
    try:
        # 获取原图片
        oldpicname = request.POST['oldpicname']
        # 菜品图片处理
        myfile = request.FILES.get("cover_pic",None)
        if not myfile:
            #return HttpResponse("没有菜品图片上传文件信息")
            cover_pic = oldpicname
        else:
            cover_pic = str(time.time())+"."+myfile.name.split('.').pop()
            destination = open("./static/uploads/product/"+cover_pic,"wb+")
            for chunk in myfile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()

        ob = Product.objects.get(id=pid)
        ob.shop_id = request.POST.get('shop_id')
        print('category_id', request.POST.get('category_id'))
        ob.category_id = request.POST.get('category_id')
        ob.cover_pic  = cover_pic
        ob.name = request.POST.get('name')
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '修改成功'}

        #判断并删除旧的图片
        if myfile:
            os.remove("./static/uploads/product/"+oldpicname)

    except Exception as err:
        print(err)
        context = {'info': '修改失败'}
    return render(request, 'myadmin/info.html', context)


