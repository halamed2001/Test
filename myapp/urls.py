from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('detail', views.detail, name='detail'),
    path('search', views.search, name='search'),

    #isc
    path('isc', views.istitution_sc, name='isc'),
    path('profile_isc/<int:isc_id>', views.profile_isc, name='profile_isc'),
    path('topics', views.topics, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('reply/topic/<int:topic_id>', views.reply_topic, name='reply_topic'),
    path('login_isc', views.login_isc, name='login_isc'),

    #donneur
    path('donneur', views.donneur, name='donneur'),
    path('donneur/<int:donneur_id>', views.tbr3jdd, name='tbr3jdd'),
    path('login', views.login, name='login'),
    path('profile/<int:donneur_id>', views.profile, name='profile'),
    path('profile/<int:donneur_id>/edit', views.update_profile, name='update_profile'),
    path('profile/<int:donneur_id>/change_password', views.update_password, name='update_password'),
    path('rendez_vous', views.rendez_vous, name='rendez_vous'),
    path('confirmation_sms', views.rendevous_confirmation_sms, name='confirmation_sms'),

]