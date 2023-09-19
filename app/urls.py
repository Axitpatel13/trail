from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('about-us',views.about,name='about'),
    path('payment',views.payments,name='payment_info'),
    path('support',views.support,name='support'),
]
