import uuid

from django import forms
from django.core.exceptions import ValidationError

from forms_part_2_demos.web.model_validators import validate_max_todos_per_person
from forms_part_2_demos.web.models import Todo, Person
from forms_part_2_demos.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
            validate_text,
        ),
        error_messages={
            'required': 'Todo text must be set!'
        }
    )
    is_done = forms.BooleanField(
        required=False,
    )
    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
            # validate_priority,
            # MinValueValidator(1),
            # MaxValueValidator(10),
        ),
    )
    #
    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     pass
    #     # raise ValidationError('Error!!!!11!1!')
    #
    # def clean_is_done(self):
    #     pass


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    def clean_text(self):
        '''
        Used for:
        1. Transform data into desired format/form/state
        2. Validation
        '''
        return self.cleaned_data['text'].lower()

    # 1. Transform data into desired format/form/state
    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']

        try:
            validate_max_todos_per_person(assignee)
        except ValidationError:
            assignee = Person.objects.get(name='Unassigned')

        return assignee

    # 2. Validation
    # def clean_assignee(self):
    #     assignee = self.cleaned_data['assignee']
    #     validate_max_todos_per_person(assignee)
    #     return assignee


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name = str(uuid.uuid4())
        return profile_image

    # def clean(self):
    #     super().clean()  # After this, all values are in `cleaned_data`
    #     profile_image = self.cleaned_data['profile_image']
    #     profile_image.name = self.cleaned_data['name']
    #
