from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.reg_user,name='register'),
]
