from django.db import models
from lectur.models import *
# Create your models here.
from human.models import Employ
# Create your models here.
class Library(models.Model):
    username=models.CharField(max_length=255,null=True, unique=True)
    password=models.CharField(max_length=255,null=True)
    uid=models.ForeignKey(Employ,on_delete=models.CASCADE,null=True)
    token=models.CharField(max_length=255,null=True,unique=True)
    profile=models.ImageField(upload_to='picture',null=True)
    email=models.EmailField(null=True)
    type=models.IntegerField(null=True)
    def __str__(self):
        return self.username
   
class Book(models.Model):
    name=models.CharField(max_length=255,null=True)
    author=models.CharField(max_length=255,null=True)
    adby=models.ForeignKey(Library,on_delete=models.DO_NOTHING,null=True)
    book=models.FileField(upload_to='pdf')
    collage=models.ForeignKey(Collage,on_delete=models.DO_NOTHING,null=True)
    depart=models.ForeignKey(Departiment,on_delete=models.DO_NOTHING,null=True)
    existingPath = models.CharField(unique=True, max_length=100,null=True)
    name = models.CharField(max_length=50,null=True)
    eof = models.BooleanField(default=False)
  
    def __str__(self):
        return self.name
class Report(models.Model):
    title=models.CharField(max_length=255,null=True)
    descr=models.CharField(max_length=255,null=True)
    nost=models.IntegerField(null=True)
    nr=models.IntegerField(null=True)
    adby=models.ForeignKey(Library,on_delete=models.DO_NOTHING,null=True)
class  Movie(models.Model):
   file = models.FileField(upload_to='documents/', null=True)
   image = models.ImageField(upload_to='images/', null=True)
    
    