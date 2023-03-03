from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from hrapp.models import Employee, Department
from hrapp.forms import EmployeeForm


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'emp/index.html')

def addEmployee(request):
    if request.method=='GET':
        form = EmployeeForm()
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
    
    employees = Employee.objects.all().values()
    return render(request,'emp/addEmployee.html',{'form':form,'employees' : employees})