from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='student'
urlpatterns = [
    path('home/',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    #path('logout/',views.logout, name='logout'),
   
    path('disprofile/',views.disprofile,name='disprofile'),
    path('home/users/',views.users,name='users'),
    path('home/proimage/',views.proimage,name='proimage'),
    path('home/clear/',views.clear,name='clear'),
    path('psforgot/',views.psforgot,name='psforgot'),
    path('npass/',views.npass,name='npass'),
    path('home/ markstud/',views.markstud,name='markstud'),
    path('sendfeedback/',views.sendfeedback,name='sendfeedback'),
    path('sendfeedback/mesage/<int:id>/',views.mesage,name='mesage'),
    path('trafic/',views.trafic,name='trafic'),
    path('dashbord/',views.dashbord,name='dashbord'),
    path('regis/',views.regis,name='regis'),
    path('signout/',views.signout,name='signout'),
    path('forgot/<token>/',views.forgot,name='forgot'),
    path('transcript/',views.transcript,name='transcript'),
    path('movies/',views.movies,name='movies'),
    path('seecomp/',views.seecomp,name='seecomp'),
      
]

