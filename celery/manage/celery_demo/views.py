from django.http import JsonResponse
from celery_demo import tasks
import time
# Create your views here.

def index(request,*args,**kwargs):
    res=tasks.add.delay(1,3)
    #任务逻辑
    return JsonResponse({'status':'successful','task_id':res.task_id})