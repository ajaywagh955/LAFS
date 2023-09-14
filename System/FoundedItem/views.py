from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import founded_items_details

# Create your views here.



def founded_item(request):
    
    logged_in_user = request.user
    
    if request.method == "POST":
        name = request.POST.get('name')
        item_type = request.POST.get('item_type')
        color = request.POST.get('color')
        size = request.POST.get('size')
        brand = request.POST.get('brand')
        founded_date = request.POST.get('lost_date')
        founded_time = request.POST.get('lost_time')
        contact_name = request.POST.get('contact_name')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        additional_comments = request.POST.get('additional_comments')
        photo = request.FILES['photo']
        
        
        item = founded_items_details.objects.create(name=name,
                                                    item_type=item_type,
                                                    color=color,
                                                    size=size,
                                                    brand=brand,
                                                    founded_date=founded_date,
                                                    founded_time=founded_time,
                                                    location=location,
                                                    contact_name=contact_name,
                                                    phone_number=phone_number,
                                                    email=email,
                                                    additional_comments=additional_comments,
                                                    photo=photo
                                                    )
        item.save()
        return redirect('view/')
        
        
    return render(request,'FoundedItem/foundeditem.html')



def view_founded_items(request):
    items = founded_items_details.objects.all()
    return render(request,'FoundedItem/view.html',{"items":items})