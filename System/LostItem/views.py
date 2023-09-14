from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import lost_item_details,Names
from Account.views import *



# Create your views here.

def send_mail_after_adding_product(username, email, name, item_type, color, size, brand, lost_date, lost_time, contact_name, location, phone_number, lost_email, additional_comments, photo):
    subject = 'Item Added Successfulyy'
    message = f'Hello {username}, your lost item has been added in our system We hope it will found earlier\n\n.'
    message += f'---Details are giver below---\n'
    message += f'Item Name {name}\n'
    message += f'Item Type: {item_type}\n'    
    message += f'Color: {color}\n'
    message += f'Size: {size}\n'
    message += f'Brand: {brand}\n'
    message += f'Lost Date: {lost_date}\n'
    message += f'Lost Time: {lost_time}\n'
    message += f'Location: {location}\n'
    message += f'Contact Name: {contact_name}\n'
    message += f'Phone Number: {phone_number}\n'
    message += f'Email: {email}\n'
    message += f'Additional Comments;: {additional_comments}\n'
    message += f'Photo: {photo}\n'
    message += f'Thanks for Using Our Service'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)

@login_required(login_url="login")
def lost_item_submit(request):
    
    user_obj = request.user
    
    if request.method=="POST":
        name = request.POST.get('name')
        item_type = request.POST.get('item_type')
        color = request.POST.get('color')
        size = request.POST.get('size')
        brand = request.POST.get('brand')
        lost_date = request.POST.get('lost_date')
        lost_time = request.POST.get('lost_time')
        location = request.POST.get('location')
        contact_name = request.POST.get('contact_name')
        phone_number = request.POST.get('phone_number')
        lost_email = request.POST.get('email')
        photo = request.FILES['photo']
        additional_comments = request.POST.get('additional_comments')
        
        item = lost_item_details.objects.create(name=name,
                                                item_type=item_type,
                                                color=color,
                                                size=size,
                                                brand=brand,
                                                lost_date=lost_date,
                                                lost_time=lost_time,
                                                location=location,
                                                contact_name=contact_name,
                                                phone_number=phone_number,
                                                email=lost_email,
                                                additional_comments=additional_comments,
                                                photo=photo
                                                )
        item.save()
        
        send_mail_after_adding_product(user_obj.username,user_obj.email,
                                       name,item_type,color,size,brand,lost_date,
                                       lost_time,location,contact_name,phone_number,
                                       lost_email,additional_comments,photo)
        
        return redirect('viewlostitems')
    
    return render(request,'LostItem/index.html')




def view_lost_items(request):
    item = lost_item_details.objects.all()
    return render(request,'LostItem/view.html',{"item":item})


def search(request):
    query = request.GET['query']
    if len(query)>40:
        lost_items = []
    else:
        lost_items = lost_item_details.objects.filter(name__icontains=query)
    item = {"item":lost_items,"query":query}
    return render(request,'LostItem/search.html', item)