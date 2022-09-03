from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
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

# Create your views here.




def register(request):
    form=Createuser()
    if request.method=='POST':
        form=Createuser(request.POST)
        if form.is_valid():
              form.save()
              user=form.cleaned_data.get('username')
              messages.success(request,"registered successfully"+user)
              subject = 'welcome to GFG world'
              message = f'Hi {User.username}, thank you for registering in geeksforgeeks.'
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [User.email, ]
              send_mail( subject, message, email_from, recipient_list )
              return redirect('login')
    Context={
            'form':form
        }    
    tempa=loader.get_template('register.html')       
    return  HttpResponse(tempa.render( Context,request))

def login(request):
    
    forma=AuthenticationForm()
        
    
    if request.method=='POST':
          forma =AuthenticationForm(data=request.POST)
          if forma.is_valid():
               username = forma.cleaned_data['username']
               request.session['username'] = username
              

               return redirect('home')
        
    Context={
          'forma':forma
    }
    return render(request,'login.html',Context)
#@login_required(login_url='login') 
def index(request):
    
   if request.session.has_key('username'):
      username = request.session['username']
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
def add(request):
    users=Reg.objects.all()
    
def profile(request):
  
    
    return render(request, 'upload.html', {})
  
  
def success(request):
    return redirect('home')
   

def disprofile(request):
  
    if request.method == 'GET':
  
        
       image = Profile.objects.all().values() 
        
      
        
        
       return render(request, 'home.html',{'image':image})
   
def uprofile(request):
     x = request.POST['first']
     y = request.FILES['last']
     z=request.POST['user']
     member=Profile(name=x,image=y,uid=z)
     
     member.save()
     
     return HttpResponseRedirect(reverse('home'))
def users(request):
    user=User.objects.all().values()
    return render(request,'base.html',{'user':user})
def complent(request,id):
    database=User.objects.all().values()
   
   
    context={
       
        'database':database
    }
    return render(request,'complent.html',context)
def csave(request,id):
    x = request.POST['cfrom']
    y = request.POST['title']
    z=request.POST['descr']
    member=Complent(title=y,discription=z)   
    member.save()
    return redirect('complent')
        