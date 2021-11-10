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
    项目前台大堂点餐首页
    '''
    return redirect(reverse('web_index'))

