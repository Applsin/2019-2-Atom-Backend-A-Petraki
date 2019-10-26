from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(default=0,primary_key=True)
    name = models.CharField(max_length=32,null=False)
    nick = models.CharField(default='',max_length=64)
    avatar = models.CharField(default='',max_length=256)
