from django.urls import path
from user_profile.views import *

urlpatterns = [
    path('', user),
    #path('profile/', profile),
    path('get_users/', get_users),
    path('create_user/', create_user),
    path('contact_list/', contact_list),
    path('search_user/', search_user),
 ]