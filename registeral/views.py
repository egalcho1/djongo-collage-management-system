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
    tempa=loader.get_template('rregister.html')       
    return  HttpResponse(tempa.render( Context,request))
def login(request):
    
    forma=AuthenticationForm()
        
    
    if request.method=='POST':
          forma =AuthenticationForm(data=request.POST)
          if forma.is_valid():
               username = forma.cleaned_data['username']
               request.session['username'] = username
              

               return redirect('hom')
        
    Context={
          'forma':forma
    }
    return render(request,'rlogin.html',Context)

#@login_required(login_url='login') 
def index(request):
    
   if request.session.has_key('username'):
      username = request.session['username']
      image=Profile.objects.all()
      return render(request, 'rindex.html', {"username" : username,'image':image})
   else:
      return render(request, 'rlogin.html', {})
def student(request):
    student=User.objects.filter(is_superuser=0)
    return render(request,'rbase.html',{'student':student})
def delete(request,id):
    member=User.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request, id):
  mymember = User.objects.get(id=id)
  template = loader.get_template('rupdate.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  first = request.POST['first']
  last = request.FILES['last']
  member = User.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
def complent(request,id):
    if request.method=='POST':
        first = request.POST['title']
        last = request.POST['descr']
        member = User.objects.get(id=id)
        member=Complent(title=first,discription=last,uid=id)
        member.save()
        return HttpResponseRedirect(reverse('hom'))
    else:
        mymember = User.objects.get(id=id)
        template = loader.get_template('rcomplent.html')
        context = {
              'mymember': mymember,
               }
        return HttpResponse(template.render(context, request))
    
def complents(request,id):
    first = request.POST['title']
    last = request.FILES['descr']
    member = Complent.objects.get(id=id)
    member=Complent(title=first,discription=last,uid=id)
    member.save()
    return HttpResponseRedirect(reverse('hom'))
def departiment(request):
    if request.method=='POST':
        pass
    else:
        depart=Departiment.objects.filter().all()
        return render(request,'rdpa.html',{'depart':depart}) 