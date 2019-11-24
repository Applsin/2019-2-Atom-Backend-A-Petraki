from django import forms

class CreateUserForm(forms.Form):
    username = forms.CharField(label="Ник пользователя", max_length=50)
    first_name = forms.CharField(label="Имя", max_length=50)
    last_name = forms.CharField(label="Фамилия", max_length=50)

class SearchUserForm(forms.Form):
    username = forms.CharField(label="Ник пользователя", max_length=50)