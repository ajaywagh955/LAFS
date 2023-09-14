from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('foundeditem_page_view/',foundeditem_page_view,name="foundeditem"),
    path('lostitem_page_view/',lostitem_page_view,name="lostitem")
]
