from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donneur', views.donneur, name='donneur'),
    path('donneur/<int:donneur_id>', views.tbr3jdd, name='tbr3jdd'),
    path('search', views.search, name='search'),
    path('hopital', views.hopital, name='hopital'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('detail', views.detail, name='detail'),
    path('profile', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('update_password', views.update_password, name='update_password'),
    path('rendez_vous', views.rendez_vous, name='rendez_vous'),

]