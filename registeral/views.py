from . rimp import *
from main.imp import *
#from . import view


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
        admin=request.session['username']
        user=User.objects.get(username=admin)
        rd=Student.objects.create(fname=fname,lname=lname,sid=sid,radmin=user,email=email,password=pas)
        rd.save()
        subject = 'this is to inform you username and password from hawaasa univeristy'
        message = f'Hi {fname}, your id={sid},your password={pas}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('..')
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
       subject = 'this is to inform you that there is compliment on you from jku'
       message = f'Hi {name.fname}, complent_on={first},massage={last} from={admin}.'
       email_from = settings.EMAIL_HOST_USER
       recipient_list = [name.email, ]
       send_mail( subject, message, email_from, recipient_list )
       member.save()
       return redirect('complent/')
       # return HttpResponseRedirect(reverse('hom'))
    else:
       # mymember = User.objects.get(id=id)
        template = loader.get_template('rcomplent.html')
        member=Student.objects.all()
        context = {
              #'mymember': mymember,
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
       rol=request.POST['rol']
       age=request.POST['age']
       depa=request.POST['depa']
       fild=request.POST['fild']
       #descr=request.POST['descr']
      # admin=request.session['username']
       lectur=Lectur(username=username,rol=rol,email=email,password=password,phone=phone,exp=exp,salary=salary,gender=gender,age=age,depa=depa,fild=fild)
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
    ran= random.randint(1, 10)
    img = qrcode.make(ran)
    type(img) 
    im= img.save("main/static/main/qr/rqr.png")
    return render(request,'qr.html',{'im':im})
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
            
