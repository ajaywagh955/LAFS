from django.urls import path
from .views import *

urlpatterns = [
    path('',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('register/',registration,name="register"),
    path('varify/<auth_token>',varify,name="varify")
    # path('token/',token_send,name="token_send"),
    # path('success',Suceess,name="success"),
    # path('varify/<auth_token>',varify,name="varify"),
    # path('error',error_page,name="error")
]
