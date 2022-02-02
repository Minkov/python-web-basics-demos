from django.shortcuts import render

from employees_app.employees.models import Employee, Department


def index(request):
    employees = [e for e in Employee.objects.order_by('department__name', 'last_name', '-first_name')]
    context = {
        'number_1': 123,
        'number_2': 321,
        'number_3': 200,
        'numbers': [123, 321, 200],
        'filesize': 123548123,
        'title': 'emplOyeEs List',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid animi consequatur dolorum est eum eveniet fugiat illo, illum iure labore molestiae necessitatibus numquam odio optio provident quaerat, quas quo sapiente?',
        'employees': employees,
        'department_names': [d.name for d in Department.objects.all()],
    }

    return render(request, 'templates_examples/index.html', context)
