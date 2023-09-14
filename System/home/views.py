from django.shortcuts import render
from django.http import HttpResponse
from Account.views import *

# Create your views here.

def index(request):
    
    # user_obj = request.user
    
    # if user_obj is not None:    
    context = {
        'user_is_authenticated': request.user.is_authenticated
    }
    return render(request,'home/index.html',context)

def foundeditem_page_view(request):
    return render(request,'home/founded_items.html')

def lostitem_page_view(request):
    return render(request,'home/lost_items.html')