from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import modelform_factory, modelformset_factory
from django.urls import reverse

from forms_advanced.web.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ("created_by",)

        labels = {
            "first_name": "Enter first name:",
        }

    def __init__(self, *args, **kwargs):
        if "user" in kwargs:
            self.user = kwargs.pop("user")

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("create-person")
        self.helper.add_input(Submit('submit', 'Create person'))

    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)

        return cleaned_data

    # def clean_first_name(self):
    #     pass

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user.is_authenticated:
            instance.created_by = self.user
        instance.save()
        return instance


class BootstrapFormMixin:
    def _init_bootstrap_form(self):
        for _, field in self.fields:
            field.widget.attrs['class'] = 'form-control'


class ReadonlyFieldsMixin:
    readonly_fields = ()

    def _mark_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"
        # for _, field in self.fields.items():
        #     field.widget.attrs["readonly"] = "readonly"


class UpdatePersonForm(ReadonlyFieldsMixin, PersonForm):
    readonly_fields = ("age", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._mark_readonly_fields()


PersonForm2 = modelform_factory(Person, fields="__all__")

PersonFormSet = modelformset_factory(Person, exclude=('created_by',), extra=2, max_num=3)

# labels = {
#     'first_name': 'Fname:',
# }
#
# error_messages = {
#     'first_name': {
#
#     }
# }
