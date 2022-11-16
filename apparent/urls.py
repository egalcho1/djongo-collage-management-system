
from django.contrib import admin
from django.urls import path,include

from registeral.views import lectur
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('student/',include('main.urls',namespace='student')),
    path('admin/', admin.site.urls),
    path('', include('reg.urls',namespace='social')),
    path('lectur/',include('lectur.urls', namespace='lectur')),
    path('human/',include('human.urls',namespace='human')),
    path('registeral/', include('registeral.urls', namespace='registeral')),
    path('service/',include('service.urls',namespace='service')),
    path('library/',include('library.urls',namespace='library')),
   
  
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)