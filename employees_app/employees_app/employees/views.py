import random

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

# A function is Django view if:
# - accepts request as first param
# - returns HttpResponse
from django.shortcuts import redirect, render

# def home(request):
#     html = f'<h1>{request.method}: This is home</h1>'
#     # return HttpResponseNotFound()
#     # same as: return HttpResponse(status=404)
#     return HttpResponse(
#         html,
#         content_type='application/xml',
#         headers={
#             'x-doncho-header': 'Django',
#         },
#     )
from django.urls import reverse_lazy

from employees_app.employees.models import Department, Employee


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('custom url'))
    print('/departments/filter/by/order-by/')
    print(reverse_lazy('department details', kwargs={
        'id': 7,
    }))

    context = {
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for _ in range(16)],
    }

    return render(request, 'index.html', context)


def go_to_home(request):
    return redirect('department details', id=random.randint(1, 1024))


def not_found(request):
    # return HttpResponseNotFound()
    raise Http404()


def department_details(request, id):
    if not isinstance(id, int):
        # return 404
        pass

    return HttpResponse(f'This is department {id}, {type(id)}')


def list_departments(request):
    department = Department(
        name=f'Department {random.randint(1, 1024)}',
    )
    department.save()

    # Don't do this, this is create, not update
    department.pk = random.randint(1024, 2048)
    department.save()

    print(list(Department.objects.filter(name='Tv app')))
    print(Department.objects.get(name='Tv app'))

    print(list(Department.objects.filter(name='Tv app 2')))
    print(Department.objects.get(name__contains='app'))
    # print(Department.objects.get(name='Tv app 2'))

    Department.objects.create(
        name=f'Department {random.randint(1, 1024)}',
    )

    context = {
        # 'departments': Department.objects.filter(name__endswith='app'),
        'departments': Department.objects
            .prefetch_related('employee_set')
            .all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def create_department(request):
    return HttpResponse('Created')
