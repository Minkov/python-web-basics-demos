from django.shortcuts import render, redirect

from form_basics.web.forms import DemoForm, EmployeeForm
from form_basics.web.models import Employee


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
    else:
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            print(form.cleaned_data['department'])
            form.save()
            return redirect('index-models')

    context = {
        "form": form,
        "employee": employee,
    }

    return render(request, "web/employee_details.html", context)


def index_models(request):
    if request.method == 'GET':
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-models')

    context = {
        # "normal_employee_form": EmployeeNormalForm(),
        "employee_form": form,
        "employee_list": Employee.objects.all(),
    }

    return render(request, "web/modelform_index.html", context)


def index(request):
    form = DemoForm(
        request.POST or None,
        initial={
            "lname": "Minkov",
        })

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')

    context = {
        'employee_form': form,
    }

    return render(request, 'web/index.html', context)

# def index(request):
#     if request.method == 'GET':
#         context = {
#             "employee_form": EmployeeForm(),
#         }
#
#         return render(request, "web/index.html", context)
#
#     else:  # request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         # print(request.POST['first_name'])
#         if form.is_valid():
#             # data is valid, populate `cleaned_data`
#             print(form.cleaned_data['first_name'])
#             # use the data
#             # redirect to some URL
#             return redirect('index')
#         else:
#             context = {
#                 "employee_form": form,
#             }
#
#             return render(request, "web/index.html", context)
