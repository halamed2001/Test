from datetime import datetime, timedelta, timezone, date
from django.shortcuts import render, redirect
from django.conf import settings
from twilio.rest import Client
from django.urls import reverse_lazy, reverse
from django.contrib.auth.hashers import make_password, check_password
from myapp.forms import DonneurForm, HopitalForm, LoginForm, RendezVousForm, Tbr3jdid, UpdatePasswords, UpdateProfile
from .models import Donneur
import hashlib
from django.contrib import messages
# Create your views here.

def home(request):
    count = Donneur.objects.count()
    return render(request, 'pages/home.html',{'count':count})


def donneur(request):
    """tel = request.POST.get('tel')
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                body='',
                from_=settings.TWILIO_PHONE_NUMBER,
                to= tel
            )"""
    msg=''
    form = DonneurForm()
    if request.method == 'POST':
        form = DonneurForm(request.POST)
        if form.is_valid():
            donneur = Donneur()
            donneur.password = make_password(donneur.password)
            form.save()
            msg = 'شكرا! لقد تم تسجيلك'
            #return redirect('confirm')
           
    return render(request, 'pages/donneur.html',{'form':form,'msg':msg})

def send_sms(request):
    return render(request, 'pages/send_sms.html')

def confirm(request):
    tel = request.POST.get('tel')
    return render(request, 'pages/confirm.html',{'tel':tel})


def search(request):
    donneur = Donneur.objects.all()
    groupeSanguin = None
    if 'search_name' in request.GET:
        groupeSanguin = request.GET['search_name']
        if groupeSanguin:
            donneur = donneur.filter(groupeSanguin__icontains = groupeSanguin)

    context={
    'donneur' : donneur
    }
    return render(request, 'pages/search.html', context)

def profile(request,donneur_id):
    donneur = Donneur.objects.get(id=donneur_id)
    context = {
        'donneur':donneur
    }    
    return render(request, 'pages/profil.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        tel = request.POST['tel']
        password = request.POST['password']
        error_msg = None
        exists = Donneur.objects.filter(tel=tel, password=password).exists()
        if exists:
            donneur_id = Donneur.objects.get(tel=tel).id
            profile_url = reverse('profile', args=[donneur_id])
            return redirect(profile_url)
        else:
            error_msg = 'رقم الهاتف أو كلمة السر غير صحيحة'
            return render(request, 'pages/login.html',{'form':form, 'error_msg':error_msg})
    return render(request, 'pages/login.html',{'form':form})

def rendez_vous(request, donneur_id):
    form = RendezVousForm()
    msg =''
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'شكرا!  تم حجز موعدك نرجوا أن تكون في الموعد'
    return render(request, 'pages/rendez_vous.html',{'form':form, 'msg':msg})

def update_profile(request, donneur_id):
    donneur = Donneur.objects.get(id=donneur_id)
    form = UpdateProfile(instance=donneur)
    if request.method == 'POST':  
        form = UpdateProfile(request.POST, instance=donneur)
        if form.is_valid():
            form.save()
            return redirect('profile',donneur_id=donneur_id)
        else:
            form = UpdateProfile(instance=donneur)  
    return render(request, 'pages/update_profile.html',{'form':form})

def update_password(request, donneur_id):
    donneur = Donneur.objects.get(id=donneur_id)
    form = UpdatePasswords(instance=donneur)
    if request.method == 'POST':
        form = UpdatePasswords(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']
            if donneur.check_password(password):
                donneur.password = hashlib.md5(new_password.encode()).hexdigest()
                donneur.save()
                messages.success(request, 'تم تغيير كلمة المرور بنجاح')
                return redirect('profile',donneur_id=donneur.id)
            else:
                form.add_error('password','كلمة المرور القديمة غير صحيحة')

    return render(request, 'pages/update_password.html',{'form':form})

def hopital(request):
    msg=''
    form = HopitalForm()
    if request.method == 'POST':
        form = HopitalForm(request.POST)
        if form.is_valid():
            hopital = form.save()
            msg = 'شكرا! لقد تم تسجيلك'
    return render(request, 'pages/hopital.html',{'form':form, 'msg':msg})


def tbr3jdd(request,donneur_id):
    msg =''
    donneur = Donneur.objects.get(id=donneur_id)
    form = Tbr3jdid(instance=donneur)
    if request.method == 'POST':
        form = Tbr3jdid(request.POST, instance=donneur)
        if form.is_valid():
            form.save(commit=False)
            date_Dernier_Don= donneur.date_Dernier_Don
            if date_Dernier_Don is None or donneur.peut_don:
                donneur.date_Dernier_Don = date_Dernier_Don                
                form.save()
                msg ='يمكنك التبرع بالدم الان '
                return redirect('profile',donneur_id=donneur_id)
            
            else:
                msg = 'عذرا يجب أن يمر على اخر تبرع لك مدة اكثر من اربعة اشهر'
                form = Tbr3jdid(instance=donneur)
        else:
                form = Tbr3jdid(instance=donneur)   
        
            
        
    return render(request, 'pages/tbr3jdd.html',{'form':form, 'msg':msg})


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')


def detail(request):
    return render(request, 'pages/detail.html')
