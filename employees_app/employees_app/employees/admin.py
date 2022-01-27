from django.contrib import admin

from employees_app.employees.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'job_title', 'company')
    # pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
