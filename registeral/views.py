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
from main.models import *
from django.contrib import sessions
from django.conf import settings
from django.core.mail import send_mail




def index(request):
    
   if request.session.has_key('username'):
      username = request.session['username']
      image=Profile.objects.all()
      return render(request, 'rindex.html', {"username" : username,'image':image})
   else:
      return render(request, 'rlogin.html', {})
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
    users=User.objects.filter(is_superuser=0)
    Context={
            'form':form,
            'lectur':users
        }    
    tempa=loader.get_template('rregister.html')       
    return  HttpResponse(tempa.render( Context,request))
def login(request):

    forma=AuthenticationForm()


    if request.method=='POST':
          forma =AuthenticationForm(data=request.POST)
          if forma.is_valid():
               username = forma.cleaned_data['username']
               request.session['username'] = username
               return redirect('hom/')

    Context={
          'forma':forma
    }
    return render(request,'rlogin.html',Context)

#@login_required(login_url='login') 

def student(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        sid=request.POST['sid']
        email=request.POST['email']
        pas=request.POST['password']
        admin=request.session['username']
        user=User.objects.get(username=admin)
        rd=Student.objects.create(fname=fname,lname=lname,sid=sid,radmin=user,email=email,password=pas)
        rd.save()
        subject = 'this is to inform you username and password'
        message = f'Hi {fname}, your id={sid},your password={pas}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('hom/')
    student=Student.objects.all()
    return render(request,'rbase.html',{'student':student})
def delete(request,id):
    member=User.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request, id):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        #sid=request.POST['sid']
        #email=request.POST['email']
       # pas=request.POST['password']
        member = Student.objects.get(id=id)
        member.fname = fname
        member.lname = lname
        member.save()
        return redirect('..')
        
    mymember = Student.objects.get(id=id)
    member=Student.objects.all()
    template = loader.get_template('rupdate.html')
    context = {
    'mymember': mymember,
    'member':member
  }
    return HttpResponse(template.render(context, request))

def complent(request,id):
    if request.method=='POST':
       first = request.POST['title']
       last = request.POST['descr']
       member = Student.objects.get(id=id)
       admin=request.session['username']
       user=User.objects.get(username=admin)
       name=Student.objects.get(id=id)
       #email=Student.objects.filter(id=id)
       member=Complent.objects.create(title=first,discription=last,uid=id,username=user)
       subject = 'this is to inform you username and password'
       message = f'Hi {name}, complent on={first},massage={last}.'
       email_from = settings.EMAIL_HOST_USER
       recipient_list = [name.email, ]
       send_mail( subject, message, email_from, recipient_list )
       member.save()
       return HttpResponseRedirect(reverse('..'))
       # return HttpResponseRedirect(reverse('hom'))
    else:
        mymember = User.objects.get(id=id)
        template = loader.get_template('rcomplent.html')
        member=Student.objects.all()
        context = {
              'mymember': mymember,
               'member': member,
               }
        return HttpResponse(template.render(context, request))
    
#def complents(request,id):
   
def departiment(request):
    if request.method=='POST':
       name=request.POST['name']
       colage=request.POST['colage']
       descr=request.POST['descr']
       admin=request.session['username']
       user=User.objects.get(username=admin)
       rd=Departiment.objects.create(name=name,colage=colage,descr=descr,admin=user)
       rd.save()
       return redirect('..')
       
    else:
        depart=Departiment.objects.filter().all()
        return render(request,'rdpa.html',{'depart':depart}) 
def rdelete(request,id):
    member=Departiment.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
def lectur(request):
    if request.method=='POST':
       username=request.POST['uname']
       email=request.POST['email']
       password=request.POST['password']
       phone=request.POST['phone']
       exp=request.POST['exp']
       salary=request.POST['salary']
       gender=request.POST['gender']
       age=request.POST['age']
       depa=request.POST['depa']
       fild=request.POST['fild']
       #descr=request.POST['descr']
      # admin=request.session['username']
       lectur=Lectur(username=username,email=email,password=password,phone=phone,exp=exp,salary=salary,gender=gender,age=age,depa=depa,fild=fild)
       lectur.save()
       return redirect('../')
    else:
        student=Lectur.objects.all()
        return render(request,'lectur.html',{'student':student})
def course(request,id):
        if request.method=='POST':
            name=request.POST['name']
            ccode=request.POST['ccode']
            crdt=request.POST['crdt']
            ect=request.POST['ect']
            adby=User.objects.get(username=request.session['username'])
            dapart=Departiment.objects.get(id=id)
            course=Course(name=name,ccode=ccode,crdt=crdt,ects=ect,adby=adby,depart=dapart)
            course.save()
            return redirect('..')
            
        else:
            student=Course.objects.all()
            return render(request,'course.html',{'student':student})