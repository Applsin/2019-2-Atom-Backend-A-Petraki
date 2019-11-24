from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import *
from .forms import *

# Create your views here.
@require_http_methods(["GET", "POST"])
@csrf_exempt
def user(request):
    return render(request, 'profile_app.html')


@require_http_methods(["GET", "POST"])
@csrf_exempt
def get_users(request):
    users =User.objects.all()
    return render(request, "user/get_users.html", {"users": users})


def create_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            new_user = User.objects.create(username=username, first_name=first_name, last_name = last_name)
            return HttpResponse('пользователь успешно создан')
        else:
            return HttpResponse("invalid data")
    else:
        form = CreateUserForm()
        return render(request, "user/create_user_form.html", {"form": form})


def search_user(request):
    if request.method == "POST":
        form = SearchUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            users = User.objects.filter(username__contains=username)
            return render(request, "user/get_users.html", {"users": users})
        else:
            return HttpResponse("invalid data")
    else:
        form = SearchUserForm()
        return render(request, "user/search_user_form.html", {"form": form})


# Список пользователей,состоящих в чате (бесполезно,но пусть будет)
@require_http_methods(["GET", "POST"])
@csrf_exempt
def contact_list(request):
    list_contacts = Member.objects.all()
    return render(request, "user/get_contacts.html", {"list": list_contacts})
