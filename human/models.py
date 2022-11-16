import email
from django.db import models
from django.contrib.auth.models import User
from lectur.models import *
# Create your models here.
class Human(models.Model):
    username=models.CharField(max_length=255,unique=True,null=True)
    password=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True,unique=True)
    adby=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    token=models.CharField(max_length=255,null=True,unique=True)
class Employ(models.Model):
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
    def __str__(self):
        return self.username