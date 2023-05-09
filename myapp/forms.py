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
    
    class Meta:
        model = Donneur
        fields = ('nom', 'tel', 'password', 'groupeSanguin', 'wilaya', 'date_Dernier_Don')
        widgets = {
            'date_Dernier_Don':forms.DateInput(attrs={'type':'date'}),
        }



class Tbr3jdid (forms.ModelForm):
    class Meta:
        model = Donneur
        fields = ('nom', 'date_Dernier_Don', 'wilaya')
        widgets = {
            'date_Dernier_Don':forms.DateInput(attrs={'type':'date'}),
        }


class HopitalForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput, label='كلمة السر')
   class Meta:
        model = Hopital
        fields = '__all__'
        

class RendezVousForm(forms.ModelForm):
   class Meta:
        model = Rendez_vous
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'})
        }

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='كلمة السر')
    class Meta:
        model = Donneur
        fields = ('tel','password')        


class UpdateProfile(forms.ModelForm):
    nom = forms.CharField(max_length=250, label='الاسم')
    tel = PhoneNumberField(label='رقم الهاتف', widget=PhoneNumberPrefixWidget, region='MR')
    

    class Meta:
        model = Donneur
        fields = ('nom', 'tel', 'groupeSanguin')


class UpdatePasswords(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="كلمة المرور القديمة :")
    new_password = forms.CharField(widget=forms.PasswordInput(), label="كلمة المرور الجديدة :")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="تأكيد كلمة المرور :")
    class Meta:
        model = Donneur
        fields = ('password','new_password', 'confirm_password')
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError('كلمات المرور الجديدة لا تتطابق')
        
        return cleaned_data




