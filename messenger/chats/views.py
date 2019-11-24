from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *
from user_profile.models import *

import datetime


# def request_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].method == 'GET' or args[0].method == 'POST':
#             return function(*args, **kwargs)
#         else:
#             return JsonResponse("error 404", safe=False)
#     return wrapper


@require_http_methods(["GET", "POST"])
@csrf_exempt
def chat_app(request):
    return render(request, 'chats_app.html')


@require_http_methods(["GET", "POST"])
@csrf_exempt
def get_chats(request):
    chats = Chat.objects.all()
    return render(request, "chats/get_chats.html", {"chats": chats})

@require_http_methods(["GET", "POST"])
@csrf_exempt
def get_chat_messages(request):
    if request.method == 'POST':
        form = GetChatMessagesForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["topic"]
            messages = Message.objects.filter(chat__topic__contains=topic)
            return render(request, "chats/get_chat_messages.html", {"messages": messages})
        else:
            return HttpResponse("invalid data")
    else:
        form = GetChatMessagesForm()
        return render(request, "chats/get_chat_messages_form.html", {"form": form})

@require_http_methods(["GET", "POST"])
@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        form = CreateChatForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["topic"]
            type_chat = form.cleaned_data["is_group_chat"]
            host = form.cleaned_data["host"]
            user_creator = get_object_or_404(User, username__contains=host)
            Chat.objects.create(host=user_creator, is_group_chat=type_chat, topic=topic)
            return HttpResponse("Чат успешно создан")
        else:
            return HttpResponse("invalid data")
    else:
        form = CreateChatForm()
        return render(request, "chats/create_chat_form.html", {"form": form})

@require_http_methods(["GET", "POST"])
@csrf_exempt
def send_message(request):
    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["content"]
            sender = form.cleaned_data["sender"]
            date = datetime.date.today()
            topic = form.cleaned_data["chat"]
            sender = get_object_or_404(User, username__contains=sender)
            chat = get_object_or_404(Chat, topic__contains=topic)
            Message.objects.create(sender=sender, chat=chat, added_at=date, content=text)
            return HttpResponse("успешная отпрвка")
        else:
            return HttpResponse("invalid data")
    else:
        form = SendMessageForm()
        return render(request, "chats/send_message_form.html", {"form": form})

@require_http_methods(["GET", "POST"])
@csrf_exempt
def get_message(request):
    if request.method == 'POST':
        form = GetMessageForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            chat = form.cleaned_data["chat"]
            message = Message.objects.filter(user=user) & Message.objects.filter(chat=chat)
            return render(request, "chats/get_message.html", {"message", message})
        else:
            return HttpResponse("invalid data")
    else:
        form = GetMessageForm()
        return render(request, "chats/get_message_form.html", {"form": form})

@require_http_methods(["GET", "POST"])
@csrf_exempt
def start(request):
    return render(request, 'start_app.html')