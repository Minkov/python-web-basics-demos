from django import template

from employees_app.employees.models import Department

register = template.Library()


@register.inclusion_tag('tags/departments_list.html')
def departments_list():
    departments = Department.objects \
        .prefetch_related('employee_set')

    # context
    return {
        'departments': departments,
    }
