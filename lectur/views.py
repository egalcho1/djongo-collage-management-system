from django.shortcuts import render
from main.imp import *
# Create your views here.

def login(request):
    
   
        
    
    if request.method=='POST':
        sid=request.POST['username']
        pass1=request.POST['pass1']
       
       
        si=Lectur.objects.get(username=sid,password=pass1)
      
        if si is not None:
                  user=Lectur.objects.get(username=sid)
       
                
                  username = request.POST['username']
                  lect=Lectur.objects.get(username=username)
                  request.session['depa']=lect.depa
                  request.session['rol']=lect.rol 
                  request.session['fild']=lect.fild
                  request.session['username'] = username
                  messages.success(request,'Successfully Loggedin')
                  return redirect('lhom/')   
    return render(request,'llogin.html',{})
def lindex(request):
    
   if request.session.has_key('username'):
      username = request.session['username']
      image=Profile.objects.all()
      return render(request, 'lindex.html', {"username" : username,'image':image})
   else:
      return render(request, 'llogin.html', {})
def mark(request):
    if request.method=='POST':
        pass
    else:
        #depa=request.session['fild']
       # student=Student.objects.get(depa=depa)
       student=Student.objects.all()
       return render(request,'lmark.html',{'student':student})
def addm(request,id):
    if request.method=='POST':
       mark1=int(request.POST['mark1'])
       mark2=int(request.POST['mark2'])
       mark3=int(request.POST['mark3'])
       total=mark1+mark2+mark3
       
       adb=request.session['username']
       dep=request.session['depa']
       course=request.session['fild']
       user=Lectur.objects.get(username=adb)
       depa=Departiment.objects.get(name=dep)
       cours=Course.objects.get(name=course)
       usern=Student.objects.get(id=id)
       if total<=100 and total >=90:
           grade="A+"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<90 and total >=85:  
           grade= "A"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<85 and total >=80:  
           grade= "A-"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<80 and total >=75:  
           grade= "B+"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<75 and total >=70:  
           grade= "B"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<70 and total >=65:  
           grade= "B-"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<65 and total >=60:  
           grade= "C+"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<60 and total >=50:  
           grade= "C"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<50 and total >=40:  
           grade= "D"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       elif total<40 and total >=0:  
           grade= "F"
           mrk=Mark.objects.create(mark1=mark1,mark2=mark2,mark3=mark3,total=total,adby=user,depa=depa,cours=cours,username=usern,grade=grade)
           mrk.save()
           return redirect('..')
       else:
           print("invalid mark my exed or less than o please check it")
           return redirect('..')
       
       
    else:
        return render(request,'ldm.html',{})
     
            
