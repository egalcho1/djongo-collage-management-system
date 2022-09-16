from .views import *
from . rimp import *
from main.imp import *

def cdelete(request,id):
    cd=Calender.objects.get(id=id)
    cd.delete()
    return redirect('..')
