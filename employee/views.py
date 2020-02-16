from django.shortcuts import render, redirect
from django.http import HttpResponse

from company.models import Company
from .forms import EmployeeForms
from .models import Employee


# from django.contrib.auth import

# Create your views here.


def lists(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000')
    employees = {"employees": Employee.objects.all()}

    return render(request, "employee/list.html", employees)


def forms(request, id=0):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000')
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForms()

            class Dummy:
                pk = 0

            employee = Dummy()
            return render(request, "employee/register.html", {"form": form, "employee": employee})
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForms(instance=employee)
        return render(request, "employee/register.html", {"employee": employee, "form": form})
    else:
        if id == 0:
            print(request.POST["email"])
            form = EmployeeForms(request.POST)
            if form.is_valid():
                form.save()
            else:
                print("not work")
        else:
            employee = Employee.objects.get(pk=id)
            # employee.firstName = request.POST['firstName']
            # employee.lastName = request.POST['lastName']
            # employee.email = request.POST['email']
            # employee.phone = request.POST['phone']
            # employee.company = Company.objects.get(pk=request.POST['company'])
            form = EmployeeForms(request.POST, instance=employee)
        if form.is_valid():
            form.save()

        return redirect('http://127.0.0.1:8000/employee/list')


def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000')
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('http://127.0.0.1:8000/employee/list')
