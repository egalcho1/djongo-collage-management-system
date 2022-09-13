from email import message
from re import S
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.template import Context,loader
from django.contrib import messages
from django.urls import reverse
from .models import *
from django.contrib import sessions
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
import hashlib
import qrcode
import random





def register(request):
  
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        sid=request.POST['sid']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            
            password=pass1
           
            stu=Student(fname=fname,lname=lname,email=email,phone=phone,password=password,sid=sid)
            stu.save()
            subject = 'welcome to GFG world egalcho'
            message = f'Hi {fname}, thank you for registering in geeksforgeeks.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )

            return redirect('login')
        else:
            print("password not correct")
       
    return  render(request,'register.html',{})

def login(request):
    
   
        
    
    if request.method=='POST':
        sid=request.POST['sid']
        pass1=request.POST['pass1']
       
       
        si=Student.objects.get(sid=sid,password=pass1)
      
        if si is not None:
                  user=Student.objects.get(sid=sid)
       
                  #auth.login(request,user)
                  username = request.POST['sid']
                  request.session['sid'] = username
                  messages.success(request,'Successfully Loggedin')
                  return redirect('home')
            
             
               
                     
                     
                  
         
    return render(request,'login.html',{})
            
      
   
#@login_required(login_url='login') 
def index(request):
    
   if request.session.has_key('sid'):
      username = request.session['sid']
      image=Profile.objects.all()
      return render(request, 'index.html', {"username" : username,'image':image})
   else:
      return render(request, 'login.html', {})
def logout(request):
   logout(request)
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")



def disprofile(request):
  
    if request.method == 'GET':
  
        
       image = Profile.objects.filter(uid=request.session['sid']).order_by(-id)[:1]
        
      
        
        
       return render(request, 'index.html',{'image':image})
   

def users(request):
    i=1
    n=++i
    user=Student.objects.filter(sid= request.session['sid'])
    return render(request,'base.html',{'user':user,'n':n})


def proimage(request):
     if request.method=='POST':
         y = request.FILES['last']
         z=request.POST['user']
         member=Profile(image=y,uid=z)
     
         member.save()
     
         return HttpResponseRedirect(reverse('home'))
     else:
       user=request.session['sid']
       return render(request,'upload.html',{'user':user})
def clear(request):
    st=Student.objects.filter(sid=request.session['sid'])
    ran= random.randint(1, 10)
    img = qrcode.make('Some data here'+ran)
    type(img) 
    im= img.save("main/static/main/qr/qr.png")
    return render(request,'qr.html',{'imga':im,'st':st})
def psforgot(request):
    if request.method=='POST':
       rand= random.randint(1, 100000)  
       request.session['rand']=rand
       number=request.session['rand']
       em=request.POST['email']
       stud=Student.objects.filter(email=em)
       if stud is not None:
           subject = 'welcome to egalcho clearance form'
           message = f'Hi {rand}, please use this number to verfiy it is you.'
           email_from = settings.EMAIL_HOST_USER
           recipient_list = [em, ]
           send_mail( subject, message, email_from, recipient_list )
           return redirect('npass')
       else:
          
           print('email deas not exist')
    return render(request,'forgot.html',{})
def npass(request):
    cod=request.session['rand']
    if request.method=='POST':
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        code=request.POST['code']
        if code==cod:
            if(pass1==pass2):
                usid=request.session['sid']
                member = Student.objects.filter(sid=usid)
                member.password=pass1
                member.save()
                return redirect('login')
            else:
                print("password not match")
        else:
            print("verfication code not match")
    return render(request,'cpass.html',{})
        
    
        