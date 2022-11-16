from django.db import models
from django.contrib.auth.models import User
from lectur.models import *
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
    collage=models.ForeignKey(Collage,on_delete=models.CASCADE,null=True)
    type=models.IntegerField(null=True)
    token=models.CharField(max_length=255,null=True,unique=True)
    def __str__(self):
        return self.username
class Calender(models.Model):
    name=models.CharField(max_length=255)
    descr=models.TextField()
    event=models.CharField(max_length=255)
    eventd=models.TextField()
    adby=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    dat=models.DateField(null=True)
    dt=models.DateField(auto_now_add=True,null=True)
class Permition(models.Model):
    name=models.CharField(max_length=100,null=True)
    type=models.IntegerField(null=True)