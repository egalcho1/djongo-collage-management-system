from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'registeral'

urlpatterns = [
 path('hom/',views.index,name='hom'),
 path('',views.login,name='login'), 
 path('depart/',views.depart,name="depart"),
 path('cdele/<int:id>/',views.cdele,name="cdele"),
 path('sdepa/',views.sdepa,name="sdepa"),
 path('rscompl/<int:id>',views.rscompl,name="rscompl"),
 #path('hom/',views.index,name='hom'),  
 path('hom/register/',views.register,name='register'),   
 path('hom/student/<int:id>',views.student,name='student'),
 path('hom/student/update/<int:id>',views.update,name='update'),
 path('hom /student/delete/<int:id>',views.delete,name='delete'),
 path('hom/student/complent/<int:id>/',views.complent,name='complent'),
 #path('hom/student/complent/complents/<int:id>/',views.complents,name='complents'),
 path('hom/departiment/',views.departiment,name='departiment'),
 path('hom/departiment/rdelete/<int:id>',views.rdelete,name='rdelete'),
 path('hom/lectur/',views.lectur,name='lectur'),
 path('hom/departiment/course/<int:id>/',views.course,name='course'),
 path('hom/maker/',views.maker,name='maker'),
 path('hom/calendar/',views.calender,name='calendar'),
 path('hom/calendar/cdelete/<int:id>/',views.cdelete,name='cdelete'),
 path('hom/calendar/cupdate/<int:id>',views.cupdate,name='cupdate'),
 path('hom/mark/',views.mark,name='mark'),
 path('hom/libregister/',views.libregister,name='libregister'),
 path('dash/',views.dash,name='dash'),
 path('permition/',views.permition,name='permition'),
 path('klmrdelete/<int:id>/',views.klmrdelete,name='klmrdelete'),
 path('klmupdate/<int:id>/',views.klmupdate,name='klmupdate'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
      #  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:  
       # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
