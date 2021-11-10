from django.db import models
from datetime import datetime

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)         #名称长度限制 必须设置
    age = models.IntegerField(default=0)



class Users(models.Model):
    id = models.AutoField(primary_key=True) #主键可省略不写
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    addtime=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "myapp_users_test"  # 指定表名
