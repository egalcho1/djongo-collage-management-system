from asyncio.windows_events import NULL
import email
from email.policy import default
from pickle import TRUE
from tkinter import CASCADE, N, Widget
from turtle import title
from django.db import models
from django.contrib.auth.models import User
import time
class Reg(models.Model):
    username=models.CharField(max_length=100,unique=True)
    gender=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=255,unique=True)
    rol=models.CharField(max_length=100,null=True)
    salary=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=255,null=True)
    age=models.DateField(max_length=100,null=True)
    depart=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
class Departiment(models.Model):
    name=models.CharField(max_length=255)
    colage=models.CharField(max_length=255)
    members=models.IntegerField(null=True)
    descr=models.CharField(max_length=255,null=True)
    admin =models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    def __str__(self):
        return self.name

class Complent(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='picture',null=TRUE)
    uid=models.IntegerField(null=True)
    discription=models.TextField()
    dat=models.DateField(null=True)
    dt=models.DateField(auto_now_add=True,null=True)
    adby=models.ForeignKey(Departiment,on_delete=models.DO_NOTHING,null=True)
    cfrom=models.CharField(max_length=255,null=TRUE)
    #comfrom=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    def __str__(self):
        return self.username
class Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=TRUE)
    
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='picture',null=TRUE,default=1)
    uid=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.username
class Student(models.Model):
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    sid=models.CharField(max_length=255,unique=True)
    age=models.DateField(null=True)
    regdate=models.DateField(auto_now_add=True)
    nationality=models.CharField(max_length=255,null=True)
    father=models.CharField(max_length=255,null=True)
    focopation=models.CharField(max_length=255,null=True)
    sregion=models.CharField(max_length=255,null=True)
    zone=models.CharField(max_length=255,null=True)
    woreda=models.CharField(max_length=255,null=True)
    kebele=models.CharField(max_length=255,null=True)
    currentposion=models.CharField(max_length=255,null=True)
    phone=models.IntegerField(null=True)
    fphone=models.IntegerField(null=True)
    fage=models.DateField(null=True)
    gender=models.CharField(max_length=10,null=True)
    disablity=models.CharField(max_length=100,null=True)
    dskind=models.CharField(max_length=255,null=True)
    status=models.BooleanField(default=0)
    password=models.CharField(max_length=255,default="1234")
    email=models.EmailField(max_length=255,null=True,unique=True)
    image=models.ImageField(null=True)
    radmin=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    depa=models.ForeignKey(Departiment,  on_delete=models.DO_NOTHING,null=True)
    dorm=models.CharField(max_length=255,null=True)
    block=models.CharField(max_length=255,null=True)
class Lectur(models.Model):
    username=models.CharField(max_length=255,unique=True) 
    email=models.EmailField(unique=True,max_length=255) 
    phone=models.IntegerField()
    depa=models.CharField(max_length=255,null=True)
    fild=models.CharField(max_length=255,null=True)
    exp=models.CharField(max_length=255,null=True)
    age=models.DateField(null=True)
    dat=models.DateTimeField(auto_now_add=True,null=True)
    salary=models.IntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=255,null=True)
    rol=models.CharField(max_length=255,null=True)

class Course(models.Model):
    name=models.CharField(max_length=255,null=True)
    ccode=models.CharField(max_length=255,unique=True)
    adby=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    depart=models.ForeignKey(Departiment,on_delete=models.CASCADE,default=1)
    crdt=models.IntegerField()
    ects=models.IntegerField()
class Calender(models.Model):
    name=models.CharField(max_length=255)
    descr=models.TextField()
    event=models.CharField(max_length=255)
    eventd=models.TextField()
    adby=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    dat=models.DateField(null=True)
    dt=models.DateField(auto_now_add=True,null=True)
class Mark(models.Model):
    username=models.ForeignKey(Student,on_delete=models.DO_NOTHING,null=True)
    adby=models.ForeignKey(Lectur,on_delete=models.DO_NOTHING,null=True)
    depa=models.ForeignKey(Departiment,on_delete=models.DO_NOTHING,null=True)
    cours=models.ForeignKey(Course,on_delete=models.DO_NOTHING,null=True)
    mark1=models.IntegerField(null=True)
    mark2=models.IntegerField(null=True)
    mark3=models.IntegerField(null=True)
    mark4=models.IntegerField(null=True)
    mark5=models.IntegerField(null=True)
    mark6=models.IntegerField(null=True)
    mark7=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    grade=models.CharField(max_length=255,null=True)
    th=models.IntegerField(null=True)
    def __str__(self):
        return self.username
class Comulative(models.Model):
    ect=models.ForeignKey(Course,on_delete=models.DO_NOTHING,null=True)
    th=models.ForeignKey(Mark,on_delete=models.DO_NOTHING,null=True)
    comu=models.IntegerField(null=True)
    
    