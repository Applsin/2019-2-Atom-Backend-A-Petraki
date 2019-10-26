from django.db import models
from user_profile.models import User
from chats.models import Message
# Create your models here.
class Attachment(models.Model):
    attach_id = models.AutoField(default=0,primary_key=True)
    user_id = models.ManyToManyField(User)
    message_id = models.ManyToManyField(Message)
    type = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
