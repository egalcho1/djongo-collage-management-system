from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

from main.models import Complent, Student
from .forms import *
from .models import *
from main.imp import *
# Create your views here.
def slogin(request):
    if request.method=='POST':
       
            user=request.POST['username']
            passw=request.POST['password']
            request.session['username']=user
            lgin=Service.objects.get(username=user,password=passw)
            if lgin is not None:
               return redirect('service:home')
            else:
                return reverse('service:slogin')
   
    return render(request,'slog.html',{})
def home(request):
    user=request.session['username']
    gh=Service.objects.get(username=user)
    typ=gh.type
    return render(request,'slogin.html',{'typ':typ})
def sreg(request):
    if request.method=='POST':
        pass
    st=Student.objects.filter().all()
    return render(request,'sreg.html',{'st':st})
def dorm(request,id):
    if request.method=='POST':
        user=request.POST['block']
        passw=request.POST['room']
        sr=Student.objects.get(id=id)
        sr.block=user
        sr.dorm=passw
        sr.save()
        st=Student.objects.filter().all()
        return render(request,'sreg.html',{'st':st})
    st=Student.objects.filter().all()
    return render(request,'dorm.html',{'st':st})
def complent(request):
    pass
    st=Student.objects.filter().all()
    return render(request,'com.html',{'st':st})
def complents(request,id):
    if request.method=='POST':
      user=request.POST['block']
      passw=request.POST['room'] 
      dat=request.POST['dt']
      name=request.POST['name']   
      username=request.session['username']
      st=Service.objects.get(username=username)
      stud=Student.objects.get(id=id)
      if st.type==1:
          sector='domitor'
      
          cm=Complent(title=user,discription=passw,uid=st.id,stid=stud,sector=sector,name=name,dat=dat)
          cm.save()
          stud.comp+=1
          stud.save()
          subject='jku complent information'
          message=f'hello,{stud.sid},this is to inform you that you are complement on=,{user},explanetion=,{passw},from={sector}'
          email_from=settings.EMAIL_HOST_USER
          recipient_list=[stud.email,]
          send_mail(subject,message,email_from,recipient_list)
          st=Student.objects.filter().all()
          return render(request,'com.html',{'st':st})
      elif st.type==0:
          sector="service"
          cm=Complent(title=user,discription=passw,uid=st.id,stid=stud,sector=sector,name=name,dat=dat)
          cm.save()
          stud.comp+=1
          stud.save()
          subject='jku complent information'
          message=f'hello,{stud.sid},this is to inform you that you are complement on=,{user},explanetion=,{passw},from={sector}'
          email_from=settings.EMAIL_HOST_USER
          recipient_list=[stud.email,]
          send_mail(subject,message,email_from,recipient_list)
          st=Student.objects.filter().all()
          return render(request,'com.html',{'st':st})
      elif st.type==2:
          sector="women"
          cm=Complent(title=user,discription=passw,uid=st.id,stid=stud,sector=sector,name=name,dat=dat)
          cm.save()
          stud.comp+=1
          stud.save()
          subject='jku complent information'
          message=f'hello,{stud.sid},this is to inform you that you are complement on=,{user},explanetion=,{passw},from=,{sector}'
          email_from=settings.EMAIL_HOST_USER
          recipient_list=[stud.email,]
          send_mail(subject,message,email_from,recipient_list)
          st=Student.objects.filter().all()
          return render(request,'com.html',{'st':st})
    
    st=Student.objects.filter().all()
    return render(request,'coms.html',{'st':st})
def comsee(request):
    username=request.session['username']
    std=Service.objects.get(username=username)
    if std.type==1:
        st=Complent.objects.filter(sector='domitor').all()
        return render(request,'comsee.html',{'st':st})
    elif std.type==0:
        st=Complent.objects.filter(sector='service').all()
        return render(request,'comsee.html',{'st':st})
    elif std.type==2:
        st=Complent.objects.filter(sector='women').all()
        return render(request,'comsee.html',{'st':st})
    return render(request,'comsee.html',{'st':st})
def delete(request,id):
    cm=Complent.objects.get(id=id)
    cm.delete()
    st=Student.objects.get(sid=cm.stid)
    st.comp-=1
    st.save()
    username=request.session['username']
    std=Service.objects.get(username=username)
    if std.type==1:
        st=Complent.objects.filter(sector='domitor').all()
        return render(request,'comsee.html',{'st':st})
    elif std.type==0:
        st=Complent.objects.filter(sector='service').all()
        return render(request,'comsee.html',{'st':st})
    elif std.type==2:
        st=Complent.objects.filter(sector='women').all()
        return render(request,'comsee.html',{'st':st})
    return render(request,'comsee.html',{'st':st})
def help(request):
    return render(request,'help.html',{})
def dash(request):
    stm=Student.objects.filter(gender="male").count()
    stf=Student.objects.filter(gender="femele").count()
    st=Student.objects.filter().count()
    return render(request,'dash.html',{'stm':stm,'stf':stf,'st':st})