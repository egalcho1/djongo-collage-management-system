from django.urls import path
from . import views
app_name='service'
urlpatterns = [
    path('',views.slogin,name='slogin'),
    path('home/',views.home,name='home'),
    path('sreg/',views.sreg,name='sreg'),
    path('dorm/<int:id>/',views.dorm,name='dorm'),
    path('complent/',views.complent,name='complent'),
    path('complents/<int:id>/',views.complents,name='complents'),
    path('seecomplent/',views.comsee,name='seecomplent'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('help/',views.help,name='help'),
    path('dash/',views.dash,name='dash'),
    
]

