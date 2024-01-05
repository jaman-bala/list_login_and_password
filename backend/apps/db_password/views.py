from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import EmployeeForm
from .models import Employee


@login_required
def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'password/index.html', {'form': form})


@login_required
def index(request):
    employees = Employee.objects.all()
    return render(request, "password/show.html", {'employees': employees})


@login_required
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'password/edit.html', {'employee': employee})


@login_required
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'password/edit.html', {'employee': employee})


@login_required
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("index")
