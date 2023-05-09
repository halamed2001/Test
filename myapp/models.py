from datetime import datetime, timezone
from django.db import models
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField
import hashlib

# Create your models here.

class Donneur(models.Model):
    nom = models.CharField( max_length=50, default='فاعل خير', verbose_name='الاسم', blank=True, null=True)
    tel = PhoneNumberField(verbose_name='الهاتف',region = 'MR')
    password = models.CharField(max_length=10, verbose_name='كلمةالسر')
    groupeSanguin = models.CharField(max_length=10,  choices=(('لا اعرف', 'لا اعرف'),
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('A+', 'A+')), verbose_name='زمرةالدم', blank=True, null=True)
    date_Dernier_Don = models.DateField(verbose_name='تاريخ اخر تبرع', blank=True, null=True)
    wilaya = models.CharField(max_length=30, choices=((' الحوض الشرقي', 'الحوض الشرقي'),
        ('الحوض الغربي', 'الحوض الغربي'),
        ('لعصابة', 'لعصابة'),
        ('كوركول', 'كوركول'),
        ('لبراكنة', 'لبراكنة'),
        ('ترارزة', 'ترارزة'),
        ('أدرار', 'أدرار'),
        ('انواذيبو', 'انواذيبو'),
        ('تكانت', 'تكانت'),
        ('كيديماغا', 'كيديماغا'),
        ('تيرس زمور', 'تيرس زمور'),
        ('إنشيري', 'إنشيري'),
        ('انواكشوط', 'انواكشوط')), verbose_name='الولاية', blank=True, null=True)
    def __str__(self):
        return self.nom
    def check_password(self, password):
        return self.password == hashlib.md5(password.encode()).hexdigest()
    
    def peut_don(self):
        if not self.date_Dernier_Don:
            return True
        today = datetime.date.today()
        last_donation = self.date_Dernier_Don
        difference = today - last_donation
        return difference.days >= 120 
    
    def dernier_don_accepte(self):
        if not self.date_Dernier_Don:
            return False
        delta = timezone.now().date() - self.date_Dernier_Don
        return delta.days >= 120
   
    
    class Meta:
       verbose_name = 'متبرع'
       verbose_name_plural = 'المتبرعون'




class Hopital(models.Model):
    nom = models.CharField(max_length=20, verbose_name='الاسم')
    password = models.CharField(max_length=10, verbose_name='كلمة السر')
    def __str__(self):
        return self.nom
    
    class Meta:
       verbose_name = 'مستشفى'
       verbose_name_plural = 'المستشفيات'
    



class Rendez_vous(models.Model):
    donneur_id = models.ForeignKey(Donneur, on_delete=models.CASCADE, verbose_name='المتبرع')
    date = models.DateField(verbose_name='التاريخ')
    time = models.TimeField(verbose_name='الوقت')
    lieu = models.CharField(max_length=15, verbose_name='المكان')
    def __str__(self):
        #return f"{self.date} - ({self.donneur_id.nom})"
        return f"{self.donneur_id.nom}"
    
    class Meta:
       verbose_name = 'ميعاد'
       verbose_name_plural = 'المواعيد'       