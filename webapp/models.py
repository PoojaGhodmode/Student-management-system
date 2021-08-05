from django.db import models
from django.contrib.auth.models import User

# Create your models here.
YEARS = (
    (u'FE', u'FE'),
    (u'SE', u'SE'),
    (u'TE', u'TE'),
    (u'BE', u'BE'),
)
SEM = (
    (u'1',u'1'),
    (u'2',u'2'),
)
DIV = (
    (u'A',u'A'),
    (u'B',u'B'),
)
GENDER_CHOICES = (
    (u'M', u'Male'),
    (u'F', u'Female'),
)
DAYS =(
    (u'Monday',u'Monday'),
    (u'Tuesday',u'Tuesday'),
    (u'Wednesday',u'Wednesday'),
    (u'Thursday',u'Thursday'),
    (u'Friday',u'Friday'),
)

class Department(models.Model):
    Dep_id = models.CharField(primary_key=True, max_length=10)
    dep_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name

class Course(models.Model):
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_id = models.CharField(primary_key= True, max_length=10)
    year = models.CharField(max_length=2,choices=YEARS)
    sem = models.CharField(max_length=1,choices=SEM)
    div = models.CharField(max_length=1,choices=DIV)
    
    def __str__(self):
        return self.department.dep_name+" "+self.year+" "+self.div

    def semester(self):
        num = [(1,2),(3,4),(5,6),(7,8)]
        if self.year == 'TE':
            return num[2][int(self.sem)-1]
        elif self.year == 'FE':
            return num[0][int(self.sem)-1]
        elif self.year == 'SE':
            return num[1][int(self.sem)-1]
        elif self.year == 'BE':
            return num[3][int(self.sem)-1]
        

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stud_id = models.CharField(max_length=30, unique=True)
    gender =  models.CharField(max_length=1,choices=GENDER_CHOICES)
    dob = models.DateField()
    phone_number = models.CharField(max_length=10) #add regex
    admission_date = models.DateField()
    course = models.ForeignKey(Course, null= True , on_delete=models.SET_NULL)

    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"
        
    def __str__(self):
        return self.user.first_name



class Subject(models.Model):
    subject_id = models.CharField(primary_key=True, max_length=10)
    sub_name = models.CharField(max_length=20)
    course = models.ForeignKey(Course, null = True, on_delete=models.SET_NULL)
    total_lec_alloted = models.IntegerField(default=1)


    def __str__(self):
        return self.sub_name

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=30, unique=True)
    dob = models.DateField()
    phone_number = models.CharField(max_length=10) 
    joining_date = models.DateField()
    department = models.ForeignKey(Department, null= True , on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.first_name


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, null= True , on_delete=models.SET_NULL)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.IntegerField()
    lec_id = models.CharField(max_length=20, primary_key=True)
    day = models.CharField(max_length=10, choices=DAYS)
    status = models.BooleanField(default=True)


class SubjectTeachers(models.Model):
    subject = models.ForeignKey(Subject, null= True , on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, null= True , on_delete=models.SET_NULL)
    # total_lec_taken = models.IntegerField(default=0)

    # def lec_taken(self):
        # total_lec_taken += 1

    def __str__(self):
        return self.teacher.user.first_name +"=>"+ self.subject.sub_name
'''
class StudentAttendance(models.Model):
    lecture = models.ForeignKey(Schedule,null=True,on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.user.first_name +" "+ self.lecture.subject.sub_name

'''





