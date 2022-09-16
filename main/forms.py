from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms
from .models import *

class Createuser(UserCreationForm):
        class Meta:
               model=User
               fields=['username','email','password1','password2']
               

class Complentform(forms.ModelForm):
        class Metta:
                model=Complent
                fields='__all__'
       
                          
