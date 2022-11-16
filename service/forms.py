from dataclasses import fields
from django import forms

from .models import *

class Sregister(forms.ModelForm):
    class Meta:
        model=Service
        fields=['username','password']