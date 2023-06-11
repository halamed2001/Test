from datetime import datetime, timedelta, timezone, date
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from twilio.rest import Client
from django.urls import reverse_lazy, reverse
from django.contrib.auth.hashers import make_password, check_password
from myapp.forms import ContactForm, DonneurForm, ISCForm, LoginForm, LoginISC, RendezVousForm, Tbr3jdid, TopicForm, UpdatePasswords, UpdateProfile
from .models import Donneur,Rendez_vous,Topic, ISC
from django.contrib.auth.decorators import login_required
import hashlib
from django.core.mail import send_mail
from django.contrib import messages
from .tasks import sendsms
# Create your views here.

def home(request):
    count = Donneur.objects.count()
    return render(request, 'pages/home.html',{'count':count})



def istitution_sc(request):
    msg=''
    form = ISCForm()
    if request.method == 'POST':
        form = ISCForm(request.POST)
        if form.is_valid():
            form.save()
            msg = ' :) نشكركم على إنضمامكم إلينا '
    return render(request, 'pages/hopital.html',{'form':form, 'msg':msg})

def topics(request):
    topic = Topic.objects.all()
    return render(request, 'pages/topics.html', {'topic':topic})

def reply_topic(request, topic_id):
    topic = get_object_or_404(Topic,pk=topic_id)
    return render(request, 'pages/reply.html')

#@login_required(login_url='login_isc')
def new_topic(request):
    msg=''
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            msg = ' :) تم نشر منشوركم '
    return render(request, 'pages/new_topic.html', {'form':form, 'msg':msg})

#@login_required(login_url='login_isc')
def profile_isc(request,isc_id):
    isc = get_object_or_404(ISC, id=isc_id)
    context = {
        'isc':isc
    }    
    return render(request, 'pages/profile_isc.html', context)

def login_isc(request):
    form = LoginISC()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        error_msg = None
        exists = ISC.objects.filter(email=email, password=password).exists()
        if exists:
            isc_id = Donneur.objects.get(email=email).id
            profile_url = reverse('profile_isc', args=[isc_id])
            return redirect(profile_url)
        else:
            error_msg = ' الإيميل أو كلمة السر غير صحيحة '
            return render(request, 'pages/login_isc.html',{'form':form, 'error_msg':error_msg})
    return render(request, 'pages/login_isc.html',{'form':form})




def rendez_vous(request):
    form = RendezVousForm()
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            rendevous_confirmation_sms(Rendez_vous)
            return redirect('confirmation_sms')
    else:
        form = RendezVousForm()    
    return render(request, 'pages/rendez_vous.html',{'form':form})

def rendevous_confirmation_sms(rendez_vous):
    tel = Donneur.objects.get('tel')
    acount_sid = ''
    auth_token = ''
    from_phone = ''

    client = Client(acount_sid, auth_token)
    message = client.messages.create(
        body=f'لقد تم حجز موعدك بنجاح في تاريخ{rendez_vous.date}',
        from_=from_phone,
        to=tel
    )





def donneur(request):
    form = DonneurForm()
    if request.method == 'POST':
        form = DonneurForm(request.POST)
        if form.is_valid():
            form.save()
            #sendsms()
        #return redirect('confirm')
           
    return render(request, 'pages/donneur.html',{'form':form})

def send_sms(request):
    return render(request, 'pages/send_sms.html')

@login_required(login_url='login')
def profile(request,donneur_id):
    donneur = get_object_or_404(Donneur, id=donneur_id)
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

@login_required(login_url='login')
def update_profile(request, donneur_id):
    donneur = get_object_or_404(Donneur, id=donneur_id)
    form = UpdateProfile(instance=donneur)
    if request.method == 'POST':  
        form = UpdateProfile(request.POST, instance=donneur)
        if form.is_valid():
            form.save()
            return redirect('profile',donneur_id=donneur_id)
        else:
            form = UpdateProfile(instance=donneur)  
    return render(request, 'pages/update_profile.html',{'form':form})

@login_required(login_url='login')
def update_password(request, donneur_id):
    donneur = get_object_or_404(Donneur, id=donneur_id)
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

def tbr3jdd(request,donneur_id):
    msg =''
    donneur = get_object_or_404(Donneur, id=donneur_id)
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

def confirm(request):
    tel = request.POST.get('tel')
    return render(request, 'pages/confirm.html',{'tel':tel})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']


        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        ) 

    return render(request, 'pages/contact.html')

def detail(request):
    return render(request, 'pages/detail.html')

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