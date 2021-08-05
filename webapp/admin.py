from django.contrib import admin
from webapp.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(SubjectTeachers)
# admin.site.register(StudentAttendance)

