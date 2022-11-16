from django.urls import path
from . import views

app_name='human'
urlpatterns = [
path('',views.login,name='login'),
path('hhom/',views.hindex,name='hindex'),
path('hhom/hreg/',views.hreg,name='hreg'),
path('hhom/collage/',views.collage,name='collage'),
path('service/',views.service,name='service'),
]
