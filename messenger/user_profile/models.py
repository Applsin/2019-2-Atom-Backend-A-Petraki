from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/{1}'.format(instance.username, filename)
    
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, null=True, verbose_name='Аватар')

    def __str__(self):
        return(' '.join([self.first_name, self.last_name]))

    class Meta:
        get_latest_by = 'last_login'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    chat = models.ForeignKey('chats.Chat',on_delete=models.SET_NULL,null = True)
    new_messages = models.BooleanField(default=False)
    last_read_message = models.OneToOneField('chats.Message',on_delete=models.SET_NULL,null = True)   

    class Meta:
        verbose_name = 'Участник чата'
        verbose_name_plural = 'Участники чатов'