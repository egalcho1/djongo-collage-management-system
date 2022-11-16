from asyncio.windows_events import NULL
import email
from email.policy import default
from pickle import TRUE
from tkinter import CASCADE, N, Widget
from turtle import title
from django.db import models
from django.contrib.auth.models import User
import time
from lectur.models import *




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
    image=models.ImageField(upload_to='picture/',null=True)
    radmin=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    depa=models.ForeignKey(Departiment,  on_delete=models.DO_NOTHING,null=True)
    dorm=models.CharField(max_length=255,null=True)
    block=models.CharField(max_length=255,null=True)
    year=models.IntegerField(null=True)
    sem=models.IntegerField(null=True)
    type=models.IntegerField(null=True)
    token=models.CharField(max_length=255,null=True,unique=True)
    cafe=models.CharField(max_length=255,null=True)
    comp=models.IntegerField(default=0)
    course=models.ManyToManyField(Course)
    regs=models.IntegerField(null=True)
    cimage=models.ImageField(upload_to='Cpicture/', null=True )
    class Meta:
        ordering = ['sid']
    def __str__(self):
        return self.sid
    @property
    def image_url(self):
       if self.image and hasattr(self.image, 'url'):
            return self.image_url

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
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    sid=models.CharField(max_length=255,null=True)
    grade=models.CharField(max_length=255,null=True)
    th=models.IntegerField(null=True)
    name=models.CharField(max_length=255,null=True)
    sem=models.IntegerField(null=True)
    def __str__(self):
        return self.username
class Comulative(models.Model):
    cid=models.ForeignKey(Course,on_delete=models.DO_NOTHING,null=True)
    ect=models.IntegerField(null=True)
    th=models.ForeignKey(Mark,on_delete=models.DO_NOTHING,null=True)
    comu=models.IntegerField(null=True)
    
    did=models.ForeignKey(Departiment,on_delete=models.DO_NOTHING,null=True)
    sem=models.IntegerField(null=True)
    gpa=models.IntegerField(null=True)
    stud=models.IntegerField(null=True)
    grade=models.CharField(max_length=255,null=True)
    ectt=models.IntegerField(null=True)
    gpat=models.IntegerField(null=True)
    comu=models.IntegerField(null=True)
class Complent(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='picture',null=TRUE)
    uid=models.IntegerField(null=True)
    stid=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    discription=models.TextField()
    dat=models.DateField(null=True)
    dt=models.DateField(auto_now_add=True,null=True)
    adby=models.ForeignKey(Departiment,on_delete=models.DO_NOTHING,null=True)
    cfrom=models.CharField(max_length=255,null=TRUE)
    sector=models.CharField(max_length=255,null=True)
    name=models.CharField(max_length=100,null=True)
   
    def __str__(self):
        return self.username
    
    
    