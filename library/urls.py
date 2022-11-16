from urllib.parse import urlparse
from django.urls import path 
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import EditorChartView
app_name='library'

urlpatterns = [
    path('',views.lblogin,name='lblogin'),
    path('lbhome/',views.lbhome,name='lbhome'),
    path('student/',views.student,name='student'),
    path('student/compl/<int:id>/',views.compl,name='compl'),
    path('lbhome/file/',views.file,name='file'),
    path('lregister/',views.lregister,name='lregister'),
   # path('create/', views.create_profile, name = 'create'),
    path('lbhome/report/',views.report,name='report'),
    path('lbhome/reportd/',views.reportd,name='reportd'),
    path('lbhome/chart/',EditorChartView.as_view(), name='editorChart'),
    path('lbdepa/<int:id>/',views.lbdepa,name='lbdepa'),
     path('fup/<int:id>/',views.fup,name='fup'),
     path('uplod/',views.uplod,name='uplod'),
      path('cdelete/<int:id>/',views.cdele,name='cdele'),
      path('fdel/<int:id>/',views.fdel,name="fdel"),
      
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)