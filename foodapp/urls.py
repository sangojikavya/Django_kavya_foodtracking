from django.urls import path
from .import views

urlpatterns=[
    path('',views.index, name='home'),
    path('delete/<int:id>',views.delete_food, name='del_food'),
    path('login',views.loadlogin, name='login'),
    path('home',views.Homepage, name='homepage'),
    path('register',views.loadregister, name='register'),
    path('reg',views.register),
    path('userlogin',views.Userlogin),
    path('logout',views.Userlogout,name='logout')


]