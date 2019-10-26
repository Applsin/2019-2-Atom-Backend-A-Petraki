from django.db import models
from user_profile.models import User

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True,default=0)
    is_group_chat = models.BooleanField(null=False,default=False)
    topic = models.CharField(max_length=64,blank=True)
    last_message = models.TextField(blank=True)
    
class Message(models.Model):
    message_id = models.AutoField(primary_key=True,default=0)
    msg_chat_id = models.ForeignKey(Chat,on_delete = models.DO_NOTHING)
    user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = models.TextField(default='',null=False)
    added_at = models.DateTimeField()