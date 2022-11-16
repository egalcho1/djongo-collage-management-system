from django.db import models
from human.models import Employ
import uuid
# Create your models here.
class Service(models.Model):
    username=models.CharField(max_length=255,null=True, unique=True)
    password=models.CharField(max_length=255,null=True)
    uid=models.ForeignKey(Employ,on_delete=models.CASCADE,null=True)
    token=models.CharField(max_length=255,null=True,unique=True)
    profile=models.ImageField(upload_to='picture',null=True)
    type=models.IntegerField(null=True)
    def __str__(self):
        uid=uuid.uuid4() 
        return self.username
    