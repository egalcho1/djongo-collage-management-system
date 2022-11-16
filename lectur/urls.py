from django.urls import path
from . import views
app_name='lectur'



urlpatterns = [
    path('',views.login,name='login'),
    path('lhom/',views.lindex,name='lindex'),
    path('lhom/lcourse/',views.lcourse,name='lcourse'),
    path('lhom/feedback/',views.feedback,name='feedback'),
    path('lhom/mark/<int:id>',views.mark,name='mark'),
    path('lhom/mark/addm/<str:sid>',views.addm,name='addm'),
    #path('dean/',views.dean,name='dean'),
    path('dean/depart/',views.depart,name='depart'),
    path('dean/headreg/',views.headreg,name='headreg'),
    #path('lectur/',views.lectur,name='lectur'),
    #path('head/',views.head,name='head'),
    path('head/ncourse/',views.ncourse,name='ncourse'),
    #path('head/management/',views.management,name='management'),
    path('dean/depart/departd/<int:id>/',views.departd,name='departd'),
    path('dean/depart/departup/<int:id>/',views.departup,name='departup'),
    path('head/ncourse/hlect/<int:id>',views.nlectur,name='nlectur'),
    path('head/ncourse/hlect/addl/<int:id>',views.addlect,name='addlect'),
    #path('head/management/addmarks/<int:id>/',views.addmarks,name='addmarks'),
    path('head/addmarks/',views.addmarks,name='addmarks'),
    path('approve/<int:id>/',views.approve,name='approve'),
    path('givb/<int:id>',views.givb,name="givb"),
   
]
