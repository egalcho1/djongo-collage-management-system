from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms
from .models import *
from main.models import *

class Createuser(UserCreationForm):
        class Meta:
               model=User
               fields=['username','email','password1','password2']
class Mark(forms.ModelForm) :
        class Meta:
                model=Mark
                fields=['username','mark1','mark2','mark3']      