from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Shop, User, Category
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import random
import hashlib
import time


# Create your views here.

def index(request, pIndex=1):
    '''浏览信息'''
    smod = Category.objects
    slist = smod.filter(status__lt=9)
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = slist.filter(name__contains=kw)
        mywhere.append('keyword='+kw)
    
     # 获取并判断搜索菜品类别条件
    cid = request.GET.get("category_id", None)
    if cid:
        ulist = slist.filter(category_id=cid)
        mywhere.append('category_id='+ulist)
    
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
    
    # 遍历当前菜品分类信息并封装对应得店铺信息
    for vo in list2:
        print('vo', vo.shop_id)
        if vo.shop_id ==  4:
            vo.shop_id = 1
        sob = Shop.objects.get(id=vo.shop_id)
        vo.shopname = sob.name

    context = {'categorylist': list2, 'plist': plist, 'pIndex': pIndex, 'maxpage':maxpage, 'mywhere':mywhere}
    return render(request, 'myadmin/category/index.html', context)

def loadCategory(request,sid):
    clist = Category.objects.filter(status__lt=9,shop_id=sid).values("id","name")
    #返回QuerySet对象，使用list强转成对应的菜品分类列表信息
    return JsonResponse({'data':list(clist)})

def add(request):
    '''
    加载信息添加表单
    ''' 
    # 获取当前所有店铺
    slist = Shop.objects.values('id','name')
    # print('slist', slist)
    context = {'shoplist': slist }
    return render(request, 'myadmin/category/add.html', context)

def insert(request):
    '''
    执行信息添加
    '''
    try:
        # 实例化model，封装信息，并执行添加
        ob = Category()
        ob.shop_id = request.POST.get('shop_id')
        print('obname', ob.name)
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

def delete(request, cid=0):
    '''
    执行信息删除
    '''
    try:
        ob = Category.objects.get(id=cid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败'}
    return render(request, 'myadmin/info.html', context)
    #return JsonResponse(context)


def edit(request,cid=0):
    '''
    加载信息编辑表单
    '''
    try:
        ob = Category.objects.get(id=cid)
        context = {'category': ob}
        slist = Shop.objects.values('id','name')
        context['shoplist'] = slist 
        return render(request, 'myadmin/category/edit.html', context)
    except Exception as err:
        print(err)
        context = {'info': '没有找到要修改的数据'} 
        return render(request, 'myadmin/info.html', context)

def update(request,cid=0):
    '''执行信息编辑'''
    try:
        ob = Category.objects.get(id=cid)
        ob.shop_id = request.POST.get('shop_id')
        ob.name = request.POST.get('name')
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '修改成功'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败'}
    return render(request, 'myadmin/info.html', context)


