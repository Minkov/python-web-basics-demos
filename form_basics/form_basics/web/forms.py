from django import forms

from form_basics.web.models import Employee


class DemoForm(forms.Form):
    firstname = forms.CharField(
        max_length=35,
        required=False,
        label="First Name:",
        help_text="Enter your first name",
        # disabled=True,
    )

    lname = forms.CharField(
        max_length=35,
        required=False,
        label="Last Name:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name",
            }
        )
    )

    email = forms.EmailField(
        required=False,
    )
    # @
    # @gmail.com

    # http://
    # .com

    age = forms.IntegerField(
        required=False,
    )

    description = forms.Textarea()

    INTERESTS = (
        (7, 'Gaming'),
        (6, 'Reading'),
        (3, 'Watching'),
        (11, 'Sport'),
    )

    interests = forms.ChoiceField(
        choices=INTERESTS,
        required=False,
    )

    interests2 = forms.IntegerField(
        widget=forms.Select(choices=INTERESTS),
        required=False,
    )

    interests3 = forms.IntegerField(
        widget=forms.RadioSelect(choices=INTERESTS),
    )

    interests4 = forms.IntegerField(
        widget=forms.CheckboxSelectMultiple(choices=INTERESTS),
    )


class EmployeeNormalForm(forms.Form):
    first_name = forms.CharField(
        max_length=Employee.MAX_FIRST_NAME_LENGTH,
        required=True,
    )

    last_name = forms.CharField(
        max_length=35,
        required=True,
    )

    role = forms.IntegerField(
        widget=forms.RadioSelect(choices=Employee.ROLES),
        required=True,
    )


class EmployeeForm(forms.ModelForm):
    # department2 = forms.CharField()

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ('first_name', 'last_name',)
        # exclude = ('role',) # '__all--' - `role`

        # help_texts
        # labels
        # error_messages

        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
        }

        widgets = {
            'role': forms.RadioSelect(
                # attrs={
                #     'disabled': 'disabled',
                # }
            )
        }
