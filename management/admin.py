from django.contrib import admin
from .models import studentAttendance,TeacherAttendance

# Register your models here.
admin.site.register(studentAttendance)
admin.site.register(TeacherAttendance)