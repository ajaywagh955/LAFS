from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
import platform
from django.http import HttpRequest
from django.contrib import messages
import uuid
from .models import User_Profile

# Create your views here.



def send_mail_after_login(username, email, ip, device, browser):
    subject = 'Login Alert'
    message = f'Hello {username}, you have successfully logged in\n\n.'
    message += f'IP Address: {ip}\n'
    message += f'Device: {device}\n'
    message += f'Browser: {browser}\n'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip



def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email).first()
        
        if user_obj is None:
            messages.success(request, "User Not Found")
            return redirect('login')
        
        profile_obj = User_Profile.objects.filter(user=user_obj).first()        
        
        if not profile_obj.is_varified:
            messages.success(request, "Your account is not verified, please check your email")
            return redirect('login')
        
        user = authenticate(username=email, password=password)
        
        if user is None:
            messages.success(request, "Wrong Password")
            return redirect('login')
        
        login(request, user)
        user_ip = get_client_ip(request)
        user_device = platform.node()
        user_browser = request.META.get('HTTP_USER_AGENT', 'Unknown Browser')

        send_mail_after_login(user_obj.username, user_obj.email, user_ip, user_device, user_browser)
        
        # Get the 'next' parameter from the request's GET parameters
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
            
        else:
            return redirect('/')
    
    return render(request, 'Account/login.html')

def send_mail_after_logout(username, email, ip, device, browser):
    subject = 'Logout Alert'
    message = f'Hello {username}, you have successfully logout\n.'
    message += f'IP Address: {ip}\n'
    message += f'Device: {device}\n'
    message += f'Browser: {browser}\n'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)


@login_required(login_url="login")
def user_logout(request):
    user_obj = request.user
    logout(request)
    user_ip = get_client_ip(request)
    user_device = platform.node()
    user_browser = request.META.get('HTTP_USER_AGENT', 'Unknown Browser')

    send_mail_after_logout(user_obj.username, user_obj.email, user_ip, user_device, user_browser)
    return redirect('/')




def varify(request,auth_token):
    try:
        profile_obj = User_Profile.objects.filter(auth_token=auth_token).first()
        
        if profile_obj:
            if profile_obj.is_varified:
                messages.success(request,"Your account is already varified")
                return redirect('login')
            
            
            profile_obj.is_varified = True
            profile_obj.save()
            messages.success(request,"Your account has been varified")            
            return redirect('login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
            



def send_mail_after_registration(email,token):
    subject = 'Please varify Your Account For Using the FindInVBKCOE'
    message = f"Hii Click on the link to varify your account http://127.0.0.1:8000/account/varify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)



def registration(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        
        if password==confirm_password:
            if not User.objects.filter(username=email).exists():
                messages.success(request,"Email already taken")
                user = User.objects.create_user(username=email,password=password,email=email)
                user.save()
                
                
                auth_token = str(uuid.uuid4())
                user_obj = User_Profile.objects.create(
                    user=user,
                    full_name=full_name,
                    mobile_number=mobile_number,
                    address=address,
                    auth_token=auth_token
                )
                
                send_mail_after_registration(email,auth_token)
                return redirect('token_send')
            else:
                messages.success(request,"Email already taken")
                return redirect('register')
        else:
            messages.success(request,"Password Not Match")
            return redirect('register')
            
    return render(request,'Account/register.html')
