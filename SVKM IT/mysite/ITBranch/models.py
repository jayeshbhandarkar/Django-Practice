from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    noOfQuestion = models.IntegerField()
    pub_date = models.DateTimeField("date published")

class Department(models.Model):
    departmentName = models.CharField(max_length=200)
    headOfDepartmentName = models.CharField(max_length=200)
    departmentPhoneNo = models.IntegerField()
    departmentEmailId = models.EmailField(max_length=200)

class Employee(models.Model):
    employeeName = models.CharField(max_length=100)
    employeeDesignation = models.CharField(max_length=100)
    employeeSalary = models.IntegerField()

    def __str__(self):
        return self.employeeName
