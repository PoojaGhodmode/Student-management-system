from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, Student,Teacher,SubjectTeachers, Subject, Schedule
from management.models import studentAttendance, TeacherAttendance
# Create your views here.

def index(request):
    return render(request , 'index.html')


def loginstudent(request):
    if request.method == "POST":
        username = request.POST['student_name']
        password = request.POST['password']
        user = auth.authenticate(username= username, password = password)
        try:
            student = Student.objects.get(user = user)
        except :
            return redirect('index')
            #message and redirect to login page
        student = User.objects.get(username= username)
        if not user.is_staff :
            auth.login(request, user)
            return redirect('studenthome')
        else:
            return redirect('index')
            
@login_required(login_url='index')
def studenthome(request):
    username = request.user.username
    user = User.objects.get(username=username)
    student = Student.objects.get(user = user) 
    id = student.stud_id
    records = {}
    attendances = studentAttendance.objects.filter(stud_id=id).order_by('-date','-time')[:5]

    lecs_attended = studentAttendance.objects.filter(stud_id = id , subject__isnull=False).count()
    course = student.course
    subjects = Subject.objects.filter(course = course)
    for attend in attendances:
        if attend.subject:
            records[attend.id] = attend.record() + " - " + subjects.get(subject_id=attend.subject).sub_name
        else:
            records[attend.id] = attend.record() + " - Unverified"
    lec = 0
    lectures = {}
    for subject in subjects:
        lectures[subject.sub_name] = [subject.total_lec_alloted, lec_taken(subject),lec_attended(subject,student)]
        lec += lec_attended(subject,student)

    
    try:
        attendance_ratio = lecs_attended * 100 / lec
    except:
        attendance_ratio = 0
    
    context = {'student': student, 'records':records,'attendance_ratio':attendance_ratio,'lectures':lectures}
    return render(request, 'studenthome.html',context)

@login_required(login_url='index')
def studentinfo(request):
    username = request.user.username
    user = User.objects.get(username=username)
    student = Student.objects.get(user = user) 
    context = {'student': student}
    return render(request, 'studentinfo.html',context)

@login_required(login_url='index')
def logout(request):
    auth.logout(request)
    return redirect("/")


# =========================TEACHER PART=====================================

def loginteacher(request):
    if request.method == "POST":
        username = request.POST['teacher_name']
        password = request.POST['password']
        user = auth.authenticate(username= username, password = password)
        try:
            teacher = Teacher.objects.get(user = user)
        except :
            return redirect('index')
            #message and redirect to login page
        teacher = User.objects.get(username= username)
        if user.is_staff :
            auth.login(request, user)
            return redirect('teacherhome')
        else:
            return redirect('index')

@login_required(login_url='index')
def teacherhome(request):
    username = request.user.username
    subject_all = Subject.objects.all()
    user = User.objects.get(username=username)
    teacher = Teacher.objects.get(user = user) 
    subjects = SubjectTeachers.objects.filter(teacher= teacher)
    id = teacher.teacher_id
    records = {}
    attendances = TeacherAttendance.objects.filter(teacher_id = id).order_by('-date','-time')[:5]
    for attend in attendances:
        if attend.subject:
            records[attend.id] = attend.record() + " - " + subject_all.get(subject_id=attend.subject).sub_name
        else:
            records[attend.id] = attend.record() + " - No lecture"

    context = {'teacher': teacher, 'subjects':subjects, 'records':records}
    return render(request, 'teacherhome.html',context)

@login_required(login_url='index')
def teacherinfo(request):
    username = request.user.username
    user = User.objects.get(username=username)
    teacher = Teacher.objects.get(user = user) 
    context = {'teacher': teacher}
    return render(request, 'teacherinfo.html',context)

@login_required(login_url='index')
def studentlist(request,id):
    user = User.objects.get(username=request.user.username)
    teacher = Teacher.objects.get(user = user)
    subject = Subject.objects.get(subject_id = id)
    course = subject.course
    students = Student.objects.filter(course = course)
    context = {"students": students ,'teacher': teacher}
    return render(request, 'studentlist.html',context)

@login_required(login_url='index')
def studentdetails(request,id):
    lectures = {}
    subjects = Subject.objects.all()
    user = User.objects.get(username=request.user.username)
    teacher = Teacher.objects.get(user = user)
    student = Student.objects.get(stud_id = id)
    subject = SubjectTeachers.objects.get(teacher = teacher, subject__course=student.course)
    subject = Subject.objects.get(subject_id = subject.subject_id)
    lectures[subject.sub_name] = [subject.total_lec_alloted, lec_taken(subject),lec_attended(subject,student)]
    attendances = studentAttendance.objects.filter(stud_id=id).order_by('-date','-time')[:5]
    records = {}
    for attend in attendances:
        if attend.subject:
            records[attend.id] = attend.record() + " - " + subjects.get(subject_id=attend.subject).sub_name
        else:
            records[attend.id] = attend.record() + " - Unverified"

    context = {"student":student,"records":records,'teacher':teacher, "lectures":lectures}
    return render(request,"studentdetails.html",context)

def lec_taken(subject):
    teach = SubjectTeachers.objects.get(subject = subject)
    teacher_id = teach.teacher_id
    teacher = Teacher.objects.get(id = teacher_id)
    uid = teacher.teacher_id
    lec = TeacherAttendance.objects.filter(subject=subject.subject_id,teacher_id=uid).count()
    return lec

def lec_attended(subject,student):
    uid = student.stud_id
    lec = studentAttendance.objects.filter(subject=subject.subject_id,stud_id=uid).count()
    return lec