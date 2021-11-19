# 购物车信息管理视图文件
import hashlib
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
import random

from myadmin.models import User,Shop, Category,Product
# Create your views here.

def add(request, pid):
    '''
    添加购物车操作
    '''
    #从session中获取当前店铺中所有菜品信息,并从中获取要放入购物车的菜品
    product = request.session['productlist'][pid]
    print('product', product)
    product['num'] = 1  # 初始化当前菜品的购买量
    # 尝试从session中获取名字为cartlist的购物车信息,若没有返回{}
    cartlist = request.session.get('cartlist',{})

    # 判断当前购物车是否存在要放进购物车的菜品
    if pid in cartlist:
        cartlist[pid]['num'] += product['num'] # 增加购买量
    else:
        cartlist[pid] = product  # 放进购物车
    print('cartlist', cartlist)
    request.session['cartlist'] = cartlist
    # 跳转到点餐首页
    return redirect(reverse('web_index'))

def delete(request, pid):
    '''
    删除购物车
    '''
    # print(pid)
    cartlist = request.session['cartlist']
    # print(cartlist)
    del cartlist[pid]
    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))

def clear(request):
    '''
    清空购物车
    '''
    request.session['cartlist'] = {}
    return redirect(reverse('web_index'))

def change(request):
    '''
    修改购物车
    '''
    cartlist = request.session['cartlist']
    # print(cartlist)
    shopid = request.GET.get('pid',0)
    # print('shopid',shopid)
    num = int(request.GET.get('num',1))
    if num < 1:
        num = 1
    cartlist[shopid]['num'] = num
    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))
