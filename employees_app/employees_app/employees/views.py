from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django import forms

from employees_app.employees.models import Department, Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter first name:',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             },
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             },
#         )
#     )
#
#     egn = forms.CharField(
#         max_length=10,
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software Developer'),
#             (2, 'QA Engineer'),
#             (3, 'DevOps Specialist'),
#         )
#     )
#
#     company = forms.ChoiceField(
#         choices=((c, c) for c in Employee.COMPANIES),
#     )
#
#     age = forms.IntegerField(
#         validators=(validate_positive,)
#     )

class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot')

    class Meta:
        model = Employee
        # fields = ('first_name', 'last_name', 'egn')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'},
            )
        }


class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'},
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name', 'Last name'),
        ),
    )


def home(request):
    return render(request, 'index.html')


# def create_employee(request):
#     if request.method == 'GET':
#         context = {
#             'employee_form': EmployeeForm(),
#         }
#         return render(request, 'create.html', context)
#     else:
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             return redirect('index')
#         context = {
#             'employee_form': employee_form,
#         }
#         return render(request, 'create.html', context)

def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     egn=employee_form.cleaned_data['egn'],
            #     company=employee_form.cleaned_data['company'],
            #     department_id=1,
            # )
            # emp = Employee(
            #     **employee_form.cleaned_data,
            #     department_id=1,
            # )
            # # emp.full_clean() # explicit call validators
            # emp.save()
            employee_form.save()
            return redirect('index')
    else:
        employee_form = EmployeeForm()

    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = EditEmployeeForm(
            request.POST,
            request.FILES,
            instance=employee,
        )
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'edit.html', context)
