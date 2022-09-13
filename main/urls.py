from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


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
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
