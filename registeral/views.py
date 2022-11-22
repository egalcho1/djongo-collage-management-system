from distutils.debug import DEBUG
from this import d
from . rimp import *
from main.imp import *
from library.models import Library
import sys
#from . import view


def index(request):
    
   if request.session.has_key('username'):
      username = request.session['username']
      image=Profile.objects.all()
      cl=Calender.objects.filter()
      user=User.objects.get(username=username)
      typ=user.is_superuser
      return render(request, 'rindex.html', {"username" : username,'image':image,'cl':cl,'typ':typ})
   else:
      return render(request, 'rlogin.html', {})
def register(request):
    form=Createuser()
    if request.method=='POST':
        form=Createuser(request.POST)
        if form.is_valid():
              form.save()
              user=form.cleaned_data.get('username')
              password=form.cleaned_data.get('password')
              email=form.cleaned_data.get('email')
              messages.success(request,"registered successfully"+user)
              subject = 'this is to inform you that you are registered as registeral in jku'
              message = f'Hi {user},your username={user}..your password={password} ..thank jku.'
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [email, ]
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
        type=request.POST['type']
        sem=request.POST['sem']
        year=float(sem)/2
        dp=request.POST['dp']
        dep=Departiment.objects.get(id=dp)
        admin=request.session['username']
        user=User.objects.get(username=admin)
        rd=Student.objects.create(fname=fname,lname=lname,sid=sid,radmin=user,email=email,password=pas,type=type,sem=sem,year=year,depa=dep)
        rd.save()
        cour=Course.objects.filter(sem=sem,depart=dep)
        for m in cour:
            
            mrk=Mark.objects.create(fname=fname,lname=lname,sid=sid,sem=sem,depa=dep,cours=m)
            mrk.save()
            subject = 'this is to inform you username and password from hawaasa univeristy'
            message = f'Hi {fname}, your id={sid},your password={pas}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('..')
    student=Student.objects.all()
    depart=Departiment.objects.all()
    return render(request,'rbase.html',{'student':student,'depart':depart})
def delete(request,id):
    member=User.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('..'))
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
      user=request.POST['block']
      passw=request.POST['room'] 
      dat=request.POST['dt']
      name=request.POST['name']   
      username=request.session['username']
      st=User.objects.get(username=username)
      stud=Student.objects.get(id=id)
      
      sector='registeral'
      
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
      return render(request,'rbase.html',{'student':st})
    
     
     
    else:
       
        
        template = loader.get_template('rcomplent.html')
        member=Student.objects.all()
        context = {
              #'mymember': mymember,
               'st': member,
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
       rd=Departiment.objects.create(name=name,collage=colage,descr=descr,admin=user)
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
       rol=request.POST['rol']
       age=request.POST['age']
       dep=request.POST['depa']
       fild=request.POST['fild']
       depa=Departiment.objects.get(name=dep)
       #descr=request.POST['descr']
      # admin=request.session['username']
       collage=depa.collage
      
       lectur=Lectur(username=username,rol=rol,email=email,password=password,phone=phone,exp=exp,salary=salary,gender=gender,age=age,depa=depa,fild=fild,collage=collage)
       lectur.save()
       subject = 'your registered to jku as lecturer'
       message = f'Hi {username}, your username is{username},password {password} thank you for using.'
       email_from = settings.EMAIL_HOST_USER
       recipient_list = [email, ]
       send_mail( subject, message, email_from, recipient_list )

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
            return redirect('/hom/')
            
        else:
            student=Course.objects.all()
            return render(request,'course.html',{'student':student})
       





def maker(request):
    sys.setrecursionlimit(1500)
    #ran= random.randint(1, 10)
    st=Student.objects.filter()
    for s in st:
       img = qrcode.make(s.sid)
       type(img) 
    
       im= img.save(f'main/static/id/{s.sid}.png')
    st=Student.objects.filter()
    media=settings.MEDIA_URL
    return render(request,'rqr.html',{'im':im,'st':st,'MEDIA_URL':media})
def calender(request):
    if request.method=='POST':
        name=request.POST['name']
        descr=request.POST['descr']
        date=request.POST['dt']
        event=request.POST['event']
        edescr=request.POST['edescr']
        adb=request.session['username']
        adby=User.objects.get(username=adb)
        cale=Calender.objects.create(name=name,descr=descr,dat=date,event=event,eventd=edescr,adby=adby)
        cale.save()
        return redirect('..')
        
       
    else:
        cale=Calender.objects.all()
        return render(request,'calendar.html',{'cale':cale})
def cdelete(request,id):
     cd=Calender.objects.get(id=id)
     cd.delete()
     return redirect('..')
def cupdate(request,id):
    pass
def mark(request):
    
    if request.method=='POST':
       mark1=request.POST['mark1']
       mark2=request.POST['mark2']
       mark3=request.POST['mark3']
       adb=request.session['username']
       user=User.objects.get(username=adb)
      
       return redirect('..')
    form =Mark()
    return render(request,'mark.html',{'form':form})
def libregister(request):
    if request.method=='POST':
            username=request.POST['name']
            password=request.POST['pass1']
            email=request.POST['email']
            type=request.POST['type']
           
            lb=Library(username=username,password=password,email=email,type=type)
            lb.save()
           
           
            subject = 'your registered to jku as librarist '
            message = f'Hi {username}, your username is{username},password {password} thank you for using.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
           
            return reverse('registeral:hom')
    lk=Library.objects.filter()
    
   
    return render(request,'klm.html',{'lk':lk})
def dash(request):
    stm=Student.objects.filter(gender="male").count()
    stf=Student.objects.filter(gender="femele").count()
    dp=Departiment.objects.filter().count()
    cs=Course.objects.filter().count()
    lk=Lectur.objects.filter().count()
    stf=Student.objects.filter(gender="femele").count()
    st=Student.objects.filter().count()
    coll=Collage.objects.filter().count()
    lkm=Lectur.objects.filter(gender="male").count()
    return render(request,'dash.html',{'stm':stm,'stf':stf,'st':st,'dp':dp,'cs':cs,'lk':lk,'lkm':lkm,'coll':coll})
def permition(request):
    if request.method=='POST':
        name=request.POST['name']
        grant=request.POST['grant']
        perm=Permition.objects.get(name=name)
        perm.type=grant
        perm.save()
        st=Student.objects.filter(regs=1)
        for s in st:
            s.regs=0
         
            s.save()
      
        return render(request,'perm.html',{})
    return render(request,'perm.html',{})
def klmrdelete(request,id):
    mn=Library.objects.get(id=id)
    mn.delete()
    kl=Library.objects.filter()
    return render(request,'klm.html',{'kl':kl})
def klmupdate(request,id):
    lb=Library.objects.get(id=id)
            
