from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from models_demos.web.models import Employee, Department, Project


def index(request):
    employees = [e for e in Employee.objects.all() if e.department_id == 1]
    # employees2 = Employee.objects.filter(department_id=1) \
    employees2 = Employee.objects \
        .filter(department__name='Engineering') \
        .order_by('last_name', 'first_name')
    # `department__name` in `filter` is like `department.name`

    # `get` returns an object, not QuerySet
    # `get` returns a single object and throws when none or multiple results
    # `get` is eager and does not return a QuerySet
    # Employee.objects.get(level=Employee.LEVEL_JUNIOR)
    # get_object_or_404(Employee, level=Employee.LEVEL_REGULAR)

    Employee.objects.filter(level=Employee.LEVEL_SENIOR) \
        .first()

    department = Department.objects.get(pk=1)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)


# https://softuni.bg/trainings/3859/python-web-framework-november-2022

def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }

    return render(request, 'department-details.html', context)


def delete_employee(request, pk):
    department_pk = 4

    # When `Restricted` this must be done explicitly
    # When `Cascade` this is done implicitly
    Employee.objects.filter(department_id=department_pk) \
        .delete()
    get_object_or_404(Department, pk=department_pk) \
        .delete()

    # employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()
    #
    # # Deletes all projects with this criteria
    # Project.objects.filter() \
    #     .delete()
    #
    # # Deletes all projects
    # Project.objects.all() \
    #     .delete()
    return redirect('index')
