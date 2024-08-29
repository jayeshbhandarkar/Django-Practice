
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us',views.about, name='about_us'),
    path('contact_us', views.contact, name="contact_us"),
    path('services', views.services, name="services"),
    path('student', views.student, name="student"),
    path('add', views.addition, name='add'),
    path('insert', views.marks, name='insert'),
    path('employee/', views.employeePage, name='employee'),
    path('employeeData', views.employeeDataSave, name='employeeData'),
    path('edit-employee/<int:id>', views.editEmployeeData, name='edit-employee'),
    path('employee-list/', views.employeeList, name='employee-list'),
]   
