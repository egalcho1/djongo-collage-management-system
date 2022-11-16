from django.shortcuts import render
from human.models import Employ, Human
from main.imp import *
from lectur.models import *
from registeral.views import lectur
from service.models import Service
import uuid

# Create your views here.
def login(request):
    if request.method=='POST':
        name=request.POST['name']
        pass1=request.POST['pass1']
        log=Human.objects.get(username=name,password=pass1)
        if log is not None:
            request.session['user']=name
            return redirect('hhom/')
    return render(request,'hlogin.html',{})
def hindex(request):
    return render(request,'hindex.html',{})
def hreg(request):
    if request.method=='POST':
         fname=request.POST['fname']
         lname=request.POST['lname']
         sal=request.POST['sal']
         age=request.POST['age']
         #col=request.POST['collage']
         #depa=request.POST['dep']
         fr=request.POST['fr']
         pro=request.POST['pro']
         phone=request.POST['phone']
         email=request.POST['email']
         exp=request.POST['exp']
         #cl=Collage.objects.get(name=col)
         #dep=Departiment.objects.get(name=depa)
         emp=Employ.objects.create(fname=fname,lname=lname,salary=sal,age=age,fr=fr,pro=pro,phone=phone,email=email,exp=exp)
         emp.save()
         return redirect('..')
    lect=Lectur.objects.all()
    return render(request,'emplo.html',{'lect':lect})
def collage(request):
   
    if request.method=='POST':
        name=request.POST['name']
       
        depa=Collage.objects.create(name=name)
        depa.save()
        clo=Collage.objects.all()
        return render(request,'col.html',{'clo':clo})
    clo=Collage.objects.all()
    return render(request,'col.html',{'clo':clo})
def service(request):
    if request.method=='POST':
         username=request.POST['uname']
         password=request.POST['password']
         type =request.POST['type']
         email =request.POST['email']
         
         reg=Service(username=username,password=password,type=type)
         reg.save()
         subject='jku registration information'
         message=f'hello,{username},this is to inform you that you are registered as student servant your username=,{username},password=,{password}'
         email_from=settings.EMAIL_HOST_USER
         recipient_list=[email,]
         send_mail(subject,message,email_from,recipient_list)
         return render(request,'service.html',{})

       
    return render(request,'service.html',{})

