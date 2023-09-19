from django.shortcuts import render
from .forms import loginform
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .models import site_info,services,about_us,case_studies,contact_us,payment_request
from users.models import user


# Create your views here.
def register(request):
        if request.method == 'POST':
            wallet_address = request.POST.get('WalletAddress')
            username = request.POST.get('username')
            email = request.POST.get('email')   
            password = request.POST.get('password')
            if user.objects.filter(username=username).exists() or user.objects.filter(email=email):
                messages.error(request,'Username/Email Already Exists')
                return redirect('register')
            miner = user.objects.create_user(username=username,crypto_wallet=wallet_address,email=email,password=password,)
            miner.save()
            messages.success(request,'User Created Sucessfully')
            return redirect('login')
        return render(request,'Auth/register.html')

def login(request):
    form = loginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,'invalid credentials')
        else:
            messages.error(request,'error validating form')
    return render(request,'Auth/login.html',{'form':form})

def dashboard(request):
    if request.method == "POST":
        if request.POST.get("timer_completed") == "true":
            user_instance = user.objects.get(username=request.user.username)
            user_instance.points += 0.00005
            user_instance.save()
            messages.success(request,'Procedure Successfully Completed')
    miner = user.objects.filter(username=request.user.username).first()
    return render(request,'Dashboard/dashboard.html',{'miner':miner})

def home(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        message_of_user = contact_us(full_name=full_name,email=email,phone=phone,message=message)
        message_of_user.save()    
    
    service = services.objects.all()[:4]
    about = about_us.objects.first()
    case_studie = case_studies.objects.all()
    site_information = site_info.objects.first()
    context = {
        'services':service,
        'about_us':about,
        'case_studies':case_studie,
        'site_info':site_information,
    }
    
    return render(request,'main/index.html',context)

def about(request):
    site_information = site_info.objects.first()
    context = {
        'site_info':site_information,
    }
    return render(request,'main/about.html',context)

def profile(request):
    miner = user.objects.filter(username=request.user).first()
    payment_info = payment_request.objects.filter(user=request.user)
    context = {
        'miner' : miner,
        'payment_info': payment_info
    }
    return render(request,'profile/profile.html',context)

def payments(request):
    if request.method== 'POST':
        paypal = request.POST.get('paypal')
        payoneer = request.POST.get('payooner')
        btc = request.POST.get('btc')
        payment = payment_request(paypal_address=paypal,payoneer_address=payoneer,btc_address=btc,user=request.user)
        payment.save()
        message = messages.success(request,'Points will be deducted and Payments will be made within 24Hrs')
        return render(request,'payments/info.html',{'message':message})
    return render(request,'payments/info.html')

def support(request):
    return render (request,"support/support.html")