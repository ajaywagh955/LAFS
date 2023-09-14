from django.urls import path
from .views import *

urlpatterns = [
    path('',view_founded_items,name="view"),
    path('submit/',founded_item,name="founded_item_index")
]


founded_item