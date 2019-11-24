from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple


class SendMessageForm(forms.Form):
    content = forms.CharField(label="Сообщение", widget=forms.Textarea)
    sender = forms.CharField(label="Ник отправителя", max_length=50)
    chat = forms.CharField(label="Чат", max_length=50)


class GetChatMessagesForm(forms.Form):
    topic = forms.CharField(label="Тема", max_length=50)


class GetMessageForm(forms.Form):
    user = forms.CharField(label="Пользователь", max_length=50)
    chat = forms.CharField(label="Чат")


class CreateChatForm(forms.Form):
    topic = forms.CharField(label="Тема", max_length=50)
    is_group_chat = forms.BooleanField(label="Групповой чат" )
    host = forms.CharField(label="Ник создателя", max_length=50)