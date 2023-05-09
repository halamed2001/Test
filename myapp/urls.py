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
    path('profile/<int:donneur_id>', views.profile, name='profile'),
    path('profile/<int:donneur_id>/edit', views.update_profile, name='update_profile'),
    path('profile/<int:donneur_id>/change_password', views.update_password, name='update_password'),
    path('donneur/<int:donneur_id>/rendez_vous', views.rendez_vous, name='rendez_vous'),

]