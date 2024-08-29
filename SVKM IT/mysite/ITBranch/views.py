from django.shortcuts import render, HttpResponse, get_object_or_404
from ITBranch.models import Employee

def index(request):
    return render(request, 'index.html')

def about(request):
    context={
        'name':'Jayesh',
        'b_name':'BTech',
        'c_name':'SVKM IOT',
        'roll_no':60,
        'student_id':1001
    }
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def student(request):
    return render(request, 'student.html')

def addition(request):
    var1 = int(request.POST['fname'])
    var2 = int(request.POST['lname'])
    result = var1+var2
    return render(request, 'result.html', {'result':result})

def marks(request):
    var3 = (request.POST['sname'])
    var4 = (request.POST['srollno'])
    var5 = (request.POST['colname'])
    var6 = (request.POST['colid'])
    var7 = int(request.POST['phy'])
    var8 = int(request.POST['che'])
    var9 = int(request.POST['mat'])
    var10 = int(request.POST['eng'])
    var11 = int(request.POST['hin'])
    
    per = ((var7+var8+var9+var10+var11)*100)/500
    result_status = 'Pass'
    grade = 'D'

    if var7<40 or var8<40 or var9<40 or var10<40 or var11<40:
        grade = 'D'
        result_status = 'Fail'
    else:
        if per>80:
            grade='A'
        elif per>60:
            grade='B'
        elif per>40:
            grade='C'
        else:
            result_status = 'Fail'

    context={
        'sname':var3,
        'srollno':var4,
        'colname':var5,
        'colid':var6,
        'phy':var7,
        'che':var8,
        'mat':var9,
        'eng':var10,
        'hin':var11,
        'per':per,
        'grade':grade,
        'result_status':result_status
    }

    return render(request, 'result1.html', context)

def employeePage(request):
    emp_obj = Employee.objects.all()
    return render(request, 'employee.html', {'emp_obj': emp_obj})

def employeeDataSave(request):
    if request.method == 'POST':
        employee_name = request.POST['employee_name']
        employee_designation = request.POST['employee_designation']
        employee_salary = int(request.POST['employee_salary'])
        
        emp_id = request.POST.get('emp_id')
        if emp_id:  
            obj = get_object_or_404(Employee, id=emp_id)
            obj.employeeName = employee_name
            obj.employeeDesignation = employee_designation
            obj.employeeSalary = employee_salary
            obj.save()
        else:
            obj = Employee(employeeName=employee_name, employeeDesignation=employee_designation, employeeSalary=employee_salary)
            obj.save()

    emp_obj = Employee.objects.all()
    return render(request, 'employee_list.html', {'emp_obj': emp_obj})

def editEmployeeData(request, id):
    emp_obj_edit = get_object_or_404(Employee, id=id)
    emp_obj = Employee.objects.all()
    return render(request, 'employee.html', {'emp_obj': emp_obj, 'emp_obj_edit': emp_obj_edit})

def employeeList(request):
    emp_obj = Employee.objects.all()
    return render(request, 'employee_list.html', {'emp_obj': emp_obj})
