from webapp.models import Teacher
from django.db import models
from webapp.models import Student
# Create your models here.

class studentAttendance(models.Model):
    stud_id = models.ForeignKey(Student, to_field='stud_id', null = True, on_delete=models.CASCADE)
    room_no = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    subject = models.CharField(max_length=10, null=True)


    def record(self):
        if not self.subject:
            subject = "Unverified"
        elif self.subject:
            subject = self.subject
        return f'{self.room_no}: {self.date} {self.time}'

    def __str__(self):
        return f'{self.stud_id} : {self.time}'


class TeacherAttendance(models.Model):
    teacher_id = models.ForeignKey(Teacher, to_field='teacher_id', null = True, on_delete=models.CASCADE)
    room_no = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    subject = models.CharField(max_length=10, null=True)


    def record(self):
        if not self.subject:
            subject = "No lecture"
        elif self.subject:
            subject = self.subject
        return f'{self.room_no}: {self.date} {self.time}'

    def __str__(self):
        return f'{self.teacher_id} : {self.time}'
