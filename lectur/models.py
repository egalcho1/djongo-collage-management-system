from django.db import models
from django.contrib.auth.models import User
#from main.models import Student
#from library.models import Library
#from service.models import Service
class Collage(models.Model):
    name=models.CharField(max_length=255,null=True)
    dean=models.CharField(max_length=255,null=True)
    ndepa=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Departiment(models.Model):
    name=models.CharField(max_length=255)
    collage=models.ForeignKey(Collage,on_delete=models.DO_NOTHING,null=True)
    members=models.IntegerField(null=True)
    descr=models.CharField(max_length=255,null=True)
    admin =models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    yearend=models.IntegerField(null=True)
    nstudent=models.IntegerField(null=True)
    nlectur=models.IntegerField(null=True)
    adby=models.CharField(max_length=255,null=True)
    hed=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Lectur(models.Model):
    username=models.CharField(max_length=255,unique=True) 
    email=models.EmailField(unique=True,max_length=255) 
    phone=models.IntegerField()
    depa=models.ForeignKey(Departiment,on_delete=models.CASCADE,null=True)
    fild=models.CharField(max_length=255,null=True)
    exp=models.CharField(max_length=255,null=True)
    age=models.DateField(null=True)
    dat=models.DateTimeField(auto_now_add=True,null=True)
    salary=models.IntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=255,null=True)
    rol=models.CharField(max_length=255,null=True)
    type=models.IntegerField(null=True)
    fr=models.CharField(max_length=255,null=True)
    pro=models.CharField(max_length=255,null=True)
    collage=models.ForeignKey(Collage,on_delete=models.DO_NOTHING,null=True)
    adress=models.CharField(max_length=255,null=True)
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    cid=models.IntegerField(null=True)
    token=models.CharField(max_length=255,null=True,unique=True)
   
    def __str__(self):
        return self.username
class Course(models.Model):
    name=models.CharField(max_length=255,null=True)
    ccode=models.CharField(max_length=255,unique=True)
    adby=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    depart=models.ForeignKey(Departiment,on_delete=models.CASCADE,default=1)
    crdt=models.IntegerField()
    ects=models.IntegerField()
    year=models.IntegerField(null=True)
    sem=models.IntegerField(null=True)
    lectur=models.ForeignKey(Lectur,on_delete=models.DO_NOTHING,null=True)
    rlt=models.CharField(max_length=255,null=True)
    add=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.ccode
class Feedback(models.Model):
    senders=models.IntegerField(null=True)
    reciverl=models.IntegerField(null=True)
    senders=models.IntegerField(null=True)
    reciverd=models.IntegerField(null=True)
    senderl=models.IntegerField(null=True)
    recivers=models.IntegerField(null=True)
    senderlb=models.IntegerField(null=True)
    reciverlb=models.IntegerField(null=True)
    senderld=models.IntegerField(null=True)
    msg=models.TextField(null=True)
    rpy=models.TextField(null=True)
    ap=models.CharField(max_length=200,null=True)
    sendap=models.CharField(max_length=100,null=True)
    dt=models.DateField(auto_now=True)

