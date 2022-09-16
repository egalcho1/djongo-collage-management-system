from email.policy import default
from pickle import TRUE
from tkinter import CASCADE, Widget
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Reg(models.Model):
    username=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    block=models.CharField(max_length=100)
    room=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    age=models.DateField(max_length=100)
    depart=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.username
class Sector(models.Model):
    name=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    memberS=models.IntegerField()
    admin =models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Complent(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='picture',null=TRUE)
    uid=models.IntegerField(null=True)
    discription=models.TextField()
    comfrom=models.ForeignKey(Sector,on_delete=models.CASCADE,default=1)
    cfrom=models.CharField(max_length=255,null=TRUE)
    def __str__(self):
        return self.username
class Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=TRUE,default=1)
    
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='picture',null=TRUE,default=1)
    uid=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.username
    