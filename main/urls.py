from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    #path('logout/',views.logout, name='logout'),
    path('home/profile/',views.profile,name='profile'),
    #path('user/<int:id>',views.user,name='user'),
    path('success/',views.success,name='success'),
    path('disprofile/',views.disprofile,name='disprofile'),
    path('home/profile/uprofile/',views.uprofile,name='uprofile'),
    path('home/users/',views.users,name='users'),
    path('home/users/complent/<int:id>/',views.complent,name='complent'),
    path('home/users/complent/<int:id>/csave/',views.csave,name='csave'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
