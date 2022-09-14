from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'registeral'

urlpatterns = [
 path('hom/',views.index,name='hom'),
 path('',views.login,name='login'), 
 #path('hom/',views.index,name='hom'),  
 path('hom/register/',views.register,name='register'),   
 path('hom/student/',views.student,name='student'),
 path('hom/student/update/<int:id>',views.update,name='update'),
 path('hom /student/delete/<int:id>',views.delete,name='delete'),
 path('hom/student/complent/<int:id>/',views.complent,name='complent'),
 #path('hom/student/complent/complents/<int:id>/',views.complents,name='complents'),
 path('hom/departiment/',views.departiment,name='departiment'),
 path('hom/departiment/rdelete/<int:id>',views.rdelete,name='rdelete'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

