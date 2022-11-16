from pickle import MARK
from django.db.models import Sum
from registeral.models import Permition
from .imp import *

from io import BytesIO
import uuid
import os
from django.core.paginator import Paginator
from library.models import Book

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
                  return redirect('student:home')
            
             
               
                     
                     
                  
         
    return render(request,'login.html',{})
            
      
   
#@login_required(login_url='login') 
def index(request):
    
   if request.session.has_key('sid'):
      username = request.session['sid']
      image=Profile.objects.all()
      ty=Student.objects.get(sid=username)
      type=ty.type
      tyr=Permition.objects.get(name='registration')
      typ=tyr.type
      return render(request, 'index.html', {"username" : username,'image':image,'type':type,'typ':typ})
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
         ag=request.POST['ag']
         fn=request.POST['fn']
         ln=request.POST['ln']
         nt=request.POST['nt']
         rg=request.POST['rg']
         zn=request.POST['zn']
         kb=request.POST['qb']
         wd=request.POST['wd']
        
         cp=request.POST['cp']
         ds=request.POST['ds']
         gd=request.POST['gd']
         pn=request.POST['pn']
         st=Student.objects.get(sid=request.session['sid'])
         st.age=ag
         st.fname=fn
         st.lname=ln
         st.nationality=nt
         st.sregion=rg
         st.zone=zn
         st.kebele=kb
         st.woreda=wd
         st.disablity=ds
        
         st.currentpostion=cp
         st.gender=gd
         st.phone=pn
         st.image=y
         st.save()
         user=request.session['sid']
         stud=Student.objects.get(sid=user)
         return render(request,'upload.html',{'user':user,'stud':stud})
         #member=Profile(image=y,uid=z)
     
          #member.save()
     
          #return HttpResponseRedirect(reverse('home'))
    #else:
    user=request.session['sid']
    return render(request,'upload.html',{'user':user})
def clear(request):
    st=Student.objects.filter(sid=request.session['sid'])
    ran= random.randint(1, 10)
    img = qrcode.make(request.session['sid'])
    type(img)
    sid=request.session['sid']
   # dir=sid
    #pdir="main/static"
   # path= os.path.join(pdir,dir)
   # if( os.path.exists(path)):
      #  im= img.save(f'main/static/{sid}/{sid}.png')
    #else:
      #  os.mkdir(path)
    im= img.save(f'main/static/qrcode/{sid}.png')
    st=Student.objects.get(sid=sid)
    st.cimage=im
    st.save()
    sid=request.session['sid']
    sd=Student.objects.get(sid=sid)
    si=sd.id
    cm=st.comp
    s=Complent.objects.filter(username=si)
    st=Student.objects.filter(sid=sid)
   
   
    return render(request,'qr.html',{'st':st,'sr':s,'cm':cm,'sid':sid})
def psforgot(request):
    if request.method=='POST':
      
       
       
       em=request.POST['email']
       rg=Student.objects.get(email=em)
       token=uuid.uuid4()
       rg.token=token
       rg.save()
       
       if rg is not None:
           subject = 'please change your password by using bello link'
           message = f'Hi {rg.fname}, please use this link to change your password.http://127.0.0.1:8000/student/forgot/{token}/'
           email_from = settings.EMAIL_HOST_USER
           recipient_list = [em, ]
           send_mail( subject, message, email_from, recipient_list )
           return render(request,'forgot.html',{})
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
def markstud(request):
    if request.method=='POST':
        id=request.POST['course']
        usid=request.session['sid']
        ui=Student.objects.get(sid=usid)
        depa=ui.depa
        se=ui.sem
        dp=Departiment.objects.get(name=depa)
        crs=Course.objects.get(id=id)
       
        cid= crs.id
        mrk=Mark.objects.filter(mark1=cid,sid=ui,depa=dp)
        cr=Course.objects.filter(depart=dp,sem=se)
        return render(request,'marke.html',{'mrk':mrk,'cr':cr})
    usid=request.session['sid']
    ui=Student.objects.get(sid=usid)
    depa=ui.depa
    se=ui.sem
    dp=Departiment.objects.get(name=depa)
    cr=Course.objects.filter(depart=dp,sem=se)
    return render(request,'marke.html',{'cr':cr})
     
    
def sendfeedback(request):
    if request.method=='POST':
       pass
    us=request.session['sid']
    st=Student.objects.get(sid=us)
    dp=st.depa
    lect=Lectur.objects.filter(depa=dp,type=1)
    return render(request,'base.html',{'lect':lect})
def mesage(request,id):
    if request.method=='POST':
       msg=request.POST['msg']
       snd=request.session['sid']
       st=Student.objects.get(sid=snd)
       id=st.id
       fd=Feedback(msg=msg,senders=id,reciverl=id)
       fd.save()
       return render(request,'ms.html',{})
    return render(request,'ms.html',{})
def trafic(request):
    return render(request,'webt.html',{})
def dashbord(request):
    st=Student.objects.filter().count()
    return render(request,'dsh.html',{'st':st})
def regis(request):
    if request.method=='POST':
        stat=request.POST['name']
        count=request.POST['account']
        st=request.session['sid']
        stud=Student.objects.get(sid=st)
        stud.cafe=stat
        stud.sem+=1
        stud.regs=1
        stud.save()
      
        tyr=Course.objects.filter(sem=stud.sem)
        for ty in tyr:
            stud=Student.objects.get(sid=st)
            std=stud.course.add(ty)
           
            mr=Mark.objects.create(sid=stud.sid,fname=stud.fname,lname=stud.lname,mark1=ty.id,sem=stud.sem,depa=stud.depa)
            mr.save()
           
        
        return render(request,'rec.html',{'tyr':tyr})
        
    tyr=Permition.objects.get(name='registration')
    typ=tyr.type
    st=request.session['sid']
    stud=Student.objects.get(sid=st)
    return render(request,'regs.html',{'typ':typ,'stud':stud})
def signout(request):
    return render(request,'login.html',{})
def forgot(request,token):
    if request.method=='POST':
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        st=Student.objects.get(token=token)
        if pass1==pass2:
            st.password=pass1
            st.save()
            return render(request,'login.html',{})
   
    return render(request,'psg.html',{})
def transcript(request):
    stud=Student.objects.get(sid=request.session['sid'])
    cm = Comulative.objects.filter(stud=stud.id).order_by('-sem')
    #items = Comulative.objects.all().aggregate(Sum('ect'))
    items =  Comulative.objects.filter().aggregate(items=Sum("ect"))["items"]
    item =  Comulative.objects.filter().aggregate(item=Sum("gpa"))["item"]
    com=item/items
    return render(request,'tr.html',{'cm':cm,'ect':items,'item':item,'com':com})
def movies(request):
       user=request.session['sid']
       st=Student.objects.get(sid=user)
       dep=st.depa
       movies = Book.objects.filter(depart=dep) 
       paginator = Paginator(movies, 4)
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)
       return render(request,"library.html",{'movies':page_obj,'book':movies})
def seecomp(request):
    sid=request.session['sid']
    st=Student.objects.get(sid=sid)
    id=st.id
    cp=Complent.objects.filter(stid=id)
    return render(request,"scp.html",{'cp':cp})
  
        
    
        