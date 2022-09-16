
from django.contrib import admin
from django.urls import path,include

from registeral.views import lectur

urlpatterns = [
    path('',include('main.urls')),
    path('admin/', admin.site.urls),
    path('registeral/', include('registeral.urls')),
    path('lectur/',include('lectur.urls')),
   
  
]
