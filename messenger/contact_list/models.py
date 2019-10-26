from django.db import models
from chats.models import Chat
# Create your models here.
class Member(models.Model):
    user_id = models.AutoField(default=0,primary_key=True)
    chat_id = models.ManyToManyField(Chat)
    new_messages = models.BooleanField(default=False)
    last_read_message_id = models.OneToOneField('chats.Message',on_delete=models.DO_NOTHING)   
