from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('loginstudent', loginstudent, name='loginstudent'),
    path('studenthome',studenthome, name="studenthome"),
    path('studentinfo',studentinfo, name="studentinfo"),
    path('loginteacher', loginteacher, name="loginteacher"),
    path('teacherhome',teacherhome, name="teacherhome"),
    path('teacherinfo',teacherinfo, name="teacherinfo"),
    path('studentlist/<str:id>',studentlist, name="studentlist"),
    path('studentlist/studentdetails/<str:id>',studentdetails, name="studentdetails"),
    path('logout',logout,name="logout"),
  
]
