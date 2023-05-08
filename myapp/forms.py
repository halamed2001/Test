import hashlib
from typing import Any, Dict
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import PasswordChangeForm
from .models import Donneur, Hopital, Rendez_vous

class DonneurForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, help_text='هذا الحقل مطلوب', label='كلمة السر')
    tel = PhoneNumberField(help_text='هذا الحقل مطلوب', label='رقم الهاتف', widget=PhoneNumberPrefixWidget, region='MR')
    def clean_password(self):
        password = self.cleaned_data['password']
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        return hashed_password
    
    class Meta:
        model = Donneur
        fields = ('nom', 'tel', 'password', 'groupeSanguin', 'wilaya')



class Tbr3jdid (forms.ModelForm):
    class Meta:
        model = Donneur
        fields = ('nom', 'date_Dernier_Don', 'wilaya')


class HopitalForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput, label='كلمة السر')
   class Meta:
        model = Hopital
        fields = '__all__'
        

class RendezVousForm(forms.ModelForm):
   class Meta:
        model = Rendez_vous
        fields = '__all__'

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='كلمة السر')
    class Meta:
        model = Donneur
        fields = ('tel','password')        


class UpdateProfile(forms.ModelForm):
    nom = forms.CharField(max_length=250, label='الاسم')
    tel = forms.IntegerField( label='الهاتف')
    groupeSanguin = forms.CharField(max_length=250, label='زمرةالدم')
    date_Dernier_Don = forms.CharField(max_length=250, label='تاريخ اخر تبرع')
    

    class Meta:
        model = Donneur
        fields = ('nom', 'tel', 'groupeSanguin', 'date_Dernier_Don')


class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0 '}), label="كلمة المرور القديمة :")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="كلمة المرور الجديدة :")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="تأكيد كلمة المرور :")
    class Meta:
        model = Donneur
        fields = ('old_password','new_password1', 'new_password2')

