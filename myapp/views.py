from django.shortcuts import render, redirect
from django.conf import settings
from twilio.rest import Client
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password, check_password
from myapp.forms import DonneurForm, HopitalForm, LoginForm, RendezVousForm, Tbr3jdid, UpdatePasswords, UpdateProfile
from .models import Donneur
import hashlib
# Create your views here.

def home(request):
    donneur = Donneur.objects.all()
    return render(request, 'pages/home.html',{'donneur':donneur})


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')


def detail(request):
    return render(request, 'pages/detail.html')

def donneur(request):
    tel = request.POST.get('tel')
    msg=''
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    form = DonneurForm()
    
    message = client.messages.create(
                body='',
                from_=settings.TWILIO_PHONE_NUMBER,
                to= tel
            )
    if request.method == 'POST':
        form = DonneurForm(request.POST)
        if form.is_valid():
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

def profile(request):
    donneur = Donneur.objects.get(donneur= request.id)
    context = {
        'donneur':donneur
    }    
    return render(request, 'pages/profil.html', context)

def login(request):
    form = LoginForm()
    return render(request, 'pages/login.html',{'form':form})

def rendez_vous(request):
    form = RendezVousForm()
    msg =''
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rendez_vous = form.save()
            msg = 'شكرا!  تم حجز موعدك نرجوا أن تكون في الموعد'
    return render(request, 'pages/rendez_vous.html',{'form':form, 'msg':msg})

def update_profile(request):
    form = UpdateProfile()

    model = Donneur
    fields = form
    template_name = "update_profile.html"
    success_url = reverse_lazy("update_profile")

    def get_object(self):
        return self.request.donneur
    
    return render(request, 'pages/update_profile.html',{'form':form})

def update_password(request):
    form = UpdatePasswords()
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
    donneur = Donneur.objects.get(id=donneur_id)
    if request.method == 'POST':
        form = Tbr3jdid(request.POST, instance=donneur)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = Tbr3jdid(instance=donneur)

    return render(request, 'pages/tbr3jdd.html',{'form':form})
