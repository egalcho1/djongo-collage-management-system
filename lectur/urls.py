from django.urls import path
from . import views
app_name='lectur'



urlpatterns = [
    path('',views.login,name='login'),
    path('lhom/',views.lindex,name='lindex'),
    path('lhom/mark/',views.mark,name='mark'),
    path('lhom/mark/addm/<int:id>/',views.addm,name='addm'),
]
