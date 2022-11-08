from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Food,Consume,Contact
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required 

# Create your views here.
def Homepage(request):
    return render(request,'home.html')

@login_required(login_url='login')
def index(request):
    
    if request.method=='POST':
        food_consumed=request.POST.get('consumed_food')
        consume=Food.objects.get(name=food_consumed)
        user=request.user
        consume=Consume(food_consume=consume,user=user)
        consume.save()
        food=Food.objects.all()
        #consumed_food=Consume.objects.filter(user=request.user)

    else:
            food=Food.objects.all() 
    consumed_food=Consume.objects.filter(user=request.user)  
    return render(request,'index.html',{'data':food,'consumed_food':consumed_food})

def delete_food(request,id):
    consumed_food=Consume.objects.get(id=id)
    if request.method=='POST':
        consumed_food.delete()    
        return redirect('/')
    else:
        return render(request,'delete.html')    

def loadlogin(request):
    return render(request,'login.html') 
               
def loadregister(request):
    return render(request,'register.html')   

def register(request):
    if request.method == 'POST':
        vfname = request.POST.get('fname')
        vlname = request.POST.get('lname')
        vuname = request.POST.get('uname')
        vemail = request.POST.get('email')
        vpasswd = request.POST.get('passwd')
        vcpasswd = request.POST.get('cpasswd')
        if vpasswd == vcpasswd:
            if User.objects.filter(username=vuname).exists():
                messages.success(request, 'Username already exist')
                return redirect('/')
            elif User.objects.filter(email=vemail).exists():
                messages.success(request, 'Email address is already registered..')
                return redirect('/')
            else:
                newuser = User.objects.create_user(first_name=vfname, last_name=vlname, username=vuname, email=vemail,
                                   password=vpasswd)
                newuser.save()
                messages.success(request, 'You have successfully registered')
                return render(request,'login.html')
                #return redirect('/userlogin')
        else:
            messages.success(request, 'Password is not matching....')
            return redirect('/')
    else:
        return render(request, 'register.html')

def Userlogin(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vpasswd=request.POST.get('passwd')
        newuser=auth.authenticate(username=vuname,password=vpasswd)
        if newuser is not None:
            auth.login(request,newuser)
            return redirect('/home')
        else:
            return render(request,'register.html')

@login_required(login_url='login')
def Userlogout(request):
    auth.logout(request)
    return render(request,'login.html') 
            
def contact(request):
    if request.method=='POST':
        vname=request.POST.get('name')
        vemail=request.POST.get('email')
        vphone=request.POST.get('phone')
        vmessage=request.POST.get('message')
        details=Contact(name=vname,email=vemail,phone=vphone,message=vmessage)
        details.save()
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')