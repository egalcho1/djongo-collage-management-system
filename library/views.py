from django.shortcuts import render,redirect,reverse
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from .models import *
from main.imp import *
from django.http import JsonResponse
from .forms import *
import os
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView,ListView
from django.contrib import messages
from django.core.paginator import Paginator
def lblogin(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['pass1']
        request.session['username']=username
        lblog=Library.objects.get(username=username,password=password)
        if lblog is  None:
           
            massage=messages.info(request,'please make sure are you registered')
            return render(request,'lblogin.html',{'massage':massage})    
            
        else:
           
            return redirect('library:lbhome')
       
    return render(request,'lblogin.html',{})


def lbhome(request):
    user=request.session['username']
    ty=Library.objects.get(username=user)
    type=ty.type
    typ=type
    return render(request,'lbhome.html',{'typ':typ})
def file(request):

     collage=Collage.objects.filter().all()
     depa=Departiment.objects.filter().all()
     
     return render(request, 'uplaods.html', context={'collage':collage})
def student(request):
    if request.method=='POST':
        id=request.POST['dep']
        depart=Departiment.objects.get(id=id)
        student=Student.objects.filter(depa=depart)
        cr=Departiment.objects.filter()
        return render(request,'stu.html',{'student':student,'cr':cr})
    cr =Departiment.objects.all()
    return render(request,'stu.html',{'cr':cr})
def compl(request,id):
    if request.method=='POST':
      user=request.POST['block']
      passw=request.POST['room'] 
      dat=request.POST['dt']
      name=request.POST['name']  
      sector="library" 
      username=request.session['username']
      st=Library.objects.get(username=username)
      stud=Student.objects.get(id=id)
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
      stu=Student.objects.get(id=id)
      com=Complent.objects.filter(stid=stu)
      return render(request,'lcomp.html',{'st':st,'com':com})
     
    
    st=Student.objects.filter().all()
   # com=Complent.objects.filter(cmd=id)
    return render(request,'lcomp.html',{'st':st})
def lregister(request):
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'file uploaded success fully')
            return render(request,'lreg.html',{'form':form})
    form=Register()
    
    return render(request,'lreg.html',{'form':form})

def report(request):
    if request.method=='POST':
         title=request.POST['title'] 
         descr=request.POST['descr']
         nost=request.POST['nost']
         nr=request.POST['nr']
         adby=request.session['username']
         lb=Library.objects.get(username=adby)
         repo=Report(title=title,descr=descr,nost=nost,nr=nr,adby=lb)
         repo.save()
         return render(request,'rep.html',{})
    return render(request,'rep.html',{})
def reportd(request):
    if request.method=='POST':
         title=request.POST['title'] 
         descr=request.POST['descr']
         nost=request.POST['nost']
         nr=request.POST['nr']
         adby=request.session['username']
         lb=Library.objects.get(username=adby)
         repo=Report(title=title,descr=descr,nost=nost,nr=nr,adby=lb)
         repo.save()
         return render(request,'rep.html',{})
    lk=Report.objects.filter().all()
    return render(request,'repod.html',{'lk':lk})
class EditorChartView(TemplateView):
    template_name = 'picahart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Library.objects.filter().count()
        return context
def lbdepa(request,id):

    
     depa=Departiment.objects.filter(collage=id).all()
     request.session['coid']=id
     
     return render(request, 'lbd.html', context={'depa':depa})
def fup(request,id):
    if request.method=='POST':
        name=request.POST['name']
        file=request.FILES['file']
       
        coll=request.session['coid']
        dep=Departiment.objects.get(id=id)
        coll=Collage.objects.get(id=coll)
        add=Library.objects.get(username=request.session['username'])
        bk=Book(name=name,book=file,collage=coll,depart=dep,adby=add)
        bk.save()
        fs=FileSystemStorage()
        fsp=fs.save(file.name,file)
        
        messages.success(request,'file uploaded success fully')
        return render(request,'fup.html',{})
        
    request.session['dpid']=id
    return render(request,'fup.html',{})
class uplod(ListView):
   model=Book
   template_name='fv.html'
   context_object_name='file'
   paginate_by= 4
   
   def uplod_view(self):
       return Book.objects.order_by('-id')
def uplod(request):
       movies = Book.objects.all() 
       paginate_by= 3
       paginator = Paginator(movies, paginate_by)
      
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)
       return render(request ,"fv.html", {'movies':page_obj,'file':movies})

def cdele(request,id):
    cm=Complent.objects.get(id=id)
    st=cm.stid
    st=Student.objects.get(sid=st)
    st.comp-=1
    st.save()
    cm.delete()
    com=Complent.objects.filter(stid=st)
    return render(request,'lcomp.html',{'st':st,'com':com})
    
    
def fdel(request,id):
    bg=Book.objects.get(id=id)
    bg.delete()
    movies = Book.objects.all() 
    paginate_by= 3
    paginator = Paginator(movies, paginate_by)
      
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request ,"fv.html", {'movies':page_obj,'file':movies})
    
   