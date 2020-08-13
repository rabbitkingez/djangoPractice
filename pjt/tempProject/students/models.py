from django.db import models

# Create your models here.

class Student(models.Model): # Table을 작성
    studentName = models.CharField(max_length=100)
    studentMajor = models.CharField(max_length=100)
    studentAge = models.IntegerField(default=0)
    studentGrade = models.IntegerField(default=0)
    studentGender = models.CharField(max_length=30)

    def __str__(self):
        return self.studentName