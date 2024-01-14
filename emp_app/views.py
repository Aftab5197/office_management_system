from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from emp_app.models import Employee


# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    employee=Employee.objects.all()
    context={
        'employee':employee
    }
    return render(request,'view.html',context)


def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        image=request.FILES['image']
        new_emp=Employee(
        first_name=first_name,
        last_name=last_name,
        dept_id=dept,
        salary=salary,
        bonus=bonus,
        role_id=role,
        phone=phone,
        hire_date=datetime.now(),
        image=image,
        )
        new_emp.save()
        return HttpResponse('successfull employee added')
    elif request.method=="GET":
        return render(request,'add.html')
    else:
        return HttpResponse('A Exception occured! Employee has been not added ')
    return render(request,'add.html')


def remove_emp(request,id=0):
    if id:
        try:
            emp_id_to_remove=Employee.objects.get(id=id)
            emp_id_to_remove.delete()
            return HttpResponse('Employee Remove Successfully')
        except:
            return HttpResponse('Please enter valid employee')
    employee = Employee.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'remove.html', context)



def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        employee=Employee.objects.all()
        if name:
            employee=employee.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            employee=employee.filter(dept__name__icontains=dept)
        if role:
            employee=employee.filter(role__name__icontains=dept)
        context={
            'employee':employee
        }
        return render(request,'view.html',context)
    elif request.method=='GET':
        return render(request,'filter.html')
    else:
        return HttpResponse('Exception Occured!')