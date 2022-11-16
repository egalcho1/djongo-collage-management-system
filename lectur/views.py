from lib2to3.pgen2.pgen import ParserGenerator
from math import radians
from re import L

from django.shortcuts import render
import lectur
from main.imp import *
import json
import this
# Create your views here.

def login(request):
    
   
        
    
    if request.method=='POST':
        sid=request.POST['username']
        pass1=request.POST['pass1']
       
       
        si=Lectur.objects.get(username=sid,password=pass1)
        
        if si is not None:
                  request.session['username'] = sid
                  lect=Lectur.objects.get(username=request.session['username'])
                  type=lect.type
                  return redirect('lectur:lindex')
    
    return render(request,'llogin.html',{})
def lindex(request):
    
   if request.session.has_key('username'):
      username = request.session['username']
       
      lect=Lectur.objects.get(username=request.session['username'])
      type=lect.type
      image=Profile.objects.all()
     
      return render(request, 'lindex.html', {"username" : username,'image':image,'type':type})
   else:
      return render(request, 'llogin.html', {})
def mark(request,id):
    ad=request.session['username']
    lk=Lectur.objects.get(username=ad)
    dbid=lk.depa
    course=Course.objects.get(id=id,lectur=lk.id,depart=dbid)
    st=Student.objects.filter(depa=course.depart,sem=course.sem)
    mark=request.session['cid']=id
    stud=Student.objects.get(depa=dbid,sem=course.sem,course=id)
    st=Student.objects.filter(depa=dbid,sem=course.sem,course=id)
    ma=Mark.objects.filter(sid=stud.sid,sem=course.sem,mark1=id)
    
    
    return render(request,'slmk.html',{'st':st,'id':id,'ma':ma})
def addm(request,sid):
    if request.method=='POST':
        quez=int(request.POST['quez'])
        ass=int(request.POST['ass'])
        mid=int(request.POST['mid'])
        final=int(request.POST['final'])
        total=quez+ass+mid+final
       
       
        adb=request.session['username']
        depa=Lectur.objects.get(username=adb)
        dep=depa.depa
        course=dep
       
      
        user=Lectur.objects.get(username=adb)
        depa=Departiment.objects.get(name=dep)
        usrn=Student.objects.get(sid=sid)
        usern=usrn.id
       
        sem=usrn.sem
        ad=request.session['username']
        lk=Lectur.objects.get(username=ad)
        cr=lk.cid
        dbid=lk.depa
        student=Student.objects.get(sid=sid)
        cid=request.session['cid']
        course=Course.objects.get(id=cid,sem=student.sem)
        cousem=course.sem
        course=Course.objects.get(id=cr)
        ct=course.ects
        if total<=100 and total>=90:
           grade='A+'
           crt=ct*4
          
           mg=Mark.objects.get(sid=sid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
          
           return render(request,'slmk.html',{'st':st,'id':id,'ma':ma})
        elif total<=90 and total>=85:
           grade='A+'
           crt=ct*4
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=85 and total>=80:
           grade='A-'
           crt=ct*3.75
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
   
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=80 and total>=75:
           grade='B+'
           crt=ct*3.5
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
           st=Student.objects.filter(depa=dbid,sem= cousem)
   
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=75 and total>=70:
           grade='B'
           crt=ct*3
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
   
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=70 and total>=65:
           grade='B-'
           crt=ct*2.75
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
   
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=65 and total>=60:
           grade='C+'
           crt=ct*2.5
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
           ma=Mark.objects.filter(sid=st.sid,sem=course.sem,mark1=cid)
          
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=60 and total>=50:
           grade='C'
           crt=ct*2
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
   
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=50 and total>=40:
           grade='D'
           crt=ct*1
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
   
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        elif total<=40 and total>=0:
           grade='F'
           crt=ct*0
           mg=Mark.objects.get(sid=sid,mark1=cid)
           mg.total=total 
           mg.grade=grade 
           mg.mark6=crt
           mg.mark2=quez
           mg.mark3=ass
           mg.mark4=mid 
           mg.mark5=final
           mg.adby=lk 
           mg.cours=course
           mg.depa=dep 
           mg.mark7=sem
           mg.save()
           ad=request.session['username']
           lk=Lectur.objects.get(username=ad)
           dbid=lk.depa
           student=Student.objects.get(sid=sid)
           cid=request.session['cid']
           course=Course.objects.get(id=cid,sem=student.sem)
           cousem=course.sem
   
   
           st=Student.objects.filter(depa=dbid,sem= cousem)
   
           ma=Mark.objects.filter(depa=dbid,cours=course.id)
           return render(request,'lmark.html',{'st':st,'id':id,'ma':ma})
        
          
          
          
        
    ad=request.session['username']
    lk=Lectur.objects.get(username=ad)
    dbid=lk.depa
    student=Student.objects.get(sid=sid)
    cid=request.session['cid']
    course=Course.objects.get(id=cid,sem=student.sem)
    cousem=course.id
   
   
   
    ma=Mark.objects.filter(sid=student.sid,sem=course.sem,mark1=cid)
    m=Mark.objects.filter(sid=sid)
    return render(request,'lk.html',{'ma':ma,'m':m})

def depart(request):
    if request.method=='POST':
        name=request.POST['name']
        descr=request.POST['descr']
        year=request.POST['year']
        admin=request.session['username']
        collage=Collage.objects.get(dean=admin)
        depa=Departiment.objects.create(name=name,descr=descr,adby=admin,yearend=year,collage=collage)
        depa.save()
        admin=request.session['username']
        colage=Collage.objects.get(dean=admin)
        dep=Departiment.objects.filter(collage=colage)
        return render(request,'depart.html',{'dep':dep})
    admin=request.session['username']
    colage=Collage.objects.get(dean=admin)
    dep=Departiment.objects.filter(collage=colage)
    
    return render(request,'depart.html',{'dep':dep})
def headreg(request):
    if request.method=='POST':
      dep=request.POST['name']
      lect=request.POST['lect']
      dp=Departiment.objects.get(name=dep)
      lct=Lectur.objects.get(username=lect)
      id=lct.id
      dp.hed=id
      ty=1
      lct.type=ty
      lct.save()
      dp.save()
      admin=request.session['username']
      colage=Collage.objects.get(dean=admin)
      dep=Departiment.objects.filter(collage=colage)
    
      return render(request,'depart.html',{'dep':dep})
    depart=Departiment.objects.filter().all()
    lectu=Lectur.objects.filter().all()
    return render(request,'hedr.html',{'depart':depart,'lect':lectu})
def departd(request,id):
    depa=Departiment.objects.get(id=id)
    depa.delete()
    return redirect('../')
def departup(request,id):
    if request.method=='POST':
        name=request.POST['name']
        descr=request.POST['descr']
        year=request.POST['year']
       
        depa=Departiment.objects.get(id=id)
        depa.name=name
        depa.descr=descr
        depa.year=year
        depa.save()
        return redirect('../')
    dp=Departiment.objects.get(id=id)
    return render(request,'dpup.html',{'dp':dp})
def lcourse(request):
    lect=Lectur.objects.get(username=request.session['username'])
    lid=lect.id
    cr=Course.objects.filter(lectur=lid)
    return render(request,'lc.html',{'cr':cr})
def ncourse(request):
    if request.method=='POST':
        name=request.POST['name']
        ccode=request.POST['ccode']
        ect=request.POST['ect']
        cr=request.POST['crt']
        sem=request.POST['sem']
        adby=request.session['username']
        dp=Lectur.objects.get(username=adby)
        depa=dp.depa
        crs=Course.objects.create(name=name,ccode=ccode,crdt=cr,ects=ect,sem=sem,depart=depa,add=adby)
        crs.save()
       
        ad=request.session['username']
        lk=Lectur.objects.get(username=ad)
        dbid=lk.depa
        course=Course.objects.filter(depart=dbid)
        return render(request,'crs.html',{'crt':course})
    ad=request.session['username']
    lk=Lectur.objects.get(username=ad)
    dbid=lk.depa
    course=Course.objects.filter(depart=dbid)
    return render(request,'crs.html',{'crt':course})
def nlectur(request,id):
    request.session['cid']=id
    ad=request.session['username']
    lk=Lectur.objects.get(username=ad)
    dbid=lk.depa
    lct=Lectur.objects.filter(depa=dbid)
    return render(request,'cid.html',{'lct':lct})
def addlect(request,id):
    cid= request.session['cid']
    lect=Lectur.objects.get(id=id)
    
    crs=Course.objects.get(id=cid)
    crs.lectur=lect
    lect.cid=crs.id
    crs.save()
    lect.save()
    ad=request.session['username']
    lk=Lectur.objects.get(username=ad)
    dbid=lk.depa
    lct=Lectur.objects.filter(depa=dbid)
    return render(request,'cid.html',{'lct':lct})
def addmarks(request):
    
     ad=request.session['username']
     lk=Lectur.objects.get(username=ad)
     dbid=lk.depa
     course=Course.objects.filter(depart=dbid,lectur=lk.id)
   
     return render(request,'lmark.html',{'st':course,'id':id})
    #return render(request,'lmark.html',{'st':st,'id':id})
def management(request):
   
    ad=request.session['username']
    lk=Lectur.objects.get(username=ad)
    dbid=lk.depa
    course=Course.objects.filter(depart=dbid)
    return render(request,'mng.html',{'crt':course})   

def feedback(request):
    if request.method=='POST':
        pass
    ad=request.session['username']
    lt=Lectur.objects.get(username=ad)
    id=lt.id
    fr=Feedback.objects.filter(reciverl=id)
    
  
    return render(request,'feed.html',{'ms':fr})
def approve(request,id):
    
    mark=Mark.objects.filter(mark1=id)
    for n in mark:
       gpa=n.mark6
       grad=n.grade
       cours=n.mark1
       stud=n.sid
       sem=n.sem
       depa=n.depa
       coursa=Course.objects.get(id=cours)
       ect=coursa.ects
      
      
       #grade=n.grade 
       
       dp=Departiment.objects.get(name=depa)
       st=Student.objects.get(sid=stud)
      # cm=Comulative.objects.all().order_by('ect')['1:1']
       ectt=+ect
       gpat=+gpa 
       comu=gpat/ectt
       cmd=Comulative.objects.create(gpa=gpa,stud=st.id,sem=sem,did=dp,cid=coursa,ect=ect,grade=grad,ectt=ectt,gpat=gpat,comu=comu)
       cmd.save()
       ad=request.session['username']
       lk=Lectur.objects.get(username=ad)
       dbid=lk.depa
       course=Course.objects.filter(depart=dbid,lectur=lk.id)
   
       return render(request,'lmark.html',{'st':course,'id':id})
    ad=request.session['username']
    lk=Lectur.objects.get(username=ad)
    dbid=lk.depa
    course=Course.objects.filter(depart=dbid,lectur=lk.id)
   
    return render(request,'lmark.html',{'st':course,'id':id})
def givb(request,id):
    
    if request.method=='POST':
        gh=request.POST['msg']
        stt=Feedback.objects.get(id=id)
        stt.rpy=gh
        stt.save()
        ad=request.session['username']
        lt=Lectur.objects.get(username=ad)
        id=lt.id
        fr=Feedback.objects.filter(id=id)
        return render(request,"fd.html",{'ms':fr})
       
    ad=request.session['username']
    lt=Lectur.objects.get(username=ad)
    id=lt.id
    fr=Feedback.objects.filter(id=id)
    
    
    return render(request,"fd.html",{'ms':fr})

        
