#from dbm.ndbm import *
from dataclasses import fields
from django import forms

from library.models import *





class UploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'book']
class Register(forms.ModelForm):
    class Meta:
        model=Library
        fields=['username','password']
class Profile_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
        'name',
        
        'book'
        ]
class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('file', 'image')

