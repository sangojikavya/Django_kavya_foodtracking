from django.urls import path
from .import views

urlpatterns=[
    path('home',views.index, name='home'),
    path('delete/<int:id>',views.delete_food, name='del_food'),
    path('login',views.loadlogin, name='login'),
    path('',views.Homepage, name='homepage'),
    path('register',views.loadregister, name='register'),
    path('reg',views.register),
    path('userlogin',views.Userlogin),
    path('logout',views.Userlogout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),

]