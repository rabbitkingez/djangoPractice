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

    return HttpResponseRedirect(reverse('student:stuAll'))