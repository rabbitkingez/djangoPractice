from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student

# Create your views here.
def regStudent(request):
    return render(request, 'students/registerStudent.html')

def regConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']


    qs = Student(
        studentName=name,
        studentMajor=major,
        studentAge=age,
        studentGrade=grade,
        studentGender=gender
    )
    qs.save()

    return HttpResponseRedirect(reverse('students:stuAll'))


def reaStudentAll(request):
    qs = Student.objects.all()
    context = {'student_list': qs}
    return render(request, 'students/readStudents.html', context)

def detStudent(request, name):
    qs = Student.objects.get(studentName = name)
    context = {'student_info' : qs}
    return render(request, 'students/detailStudent.html', context)

def reaStudentOne(request, name):
    qs = Student.objects.get(studentName = name)
    context = {'student_info' : qs}
    return render(request, 'students/modifyStudent.html', context)

def modConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    s_qs = Student.objects.get(studentName=name)
    s_qs.studentName = name
    s_qs.studentMajor = major
    s_qs.studentAge = age
    s_qs.studentGrade = grade
    s_qs.studentGender = gender

    s_qs.save()

    return HttpResponseRedirect(reverse('students:stuAll'))


def delConStudent(request, name):
    qs = Student.objects.get(studentName=name)
    qs.delete()

    return HttpResponseRedirect(reverse('students:stuAll'))