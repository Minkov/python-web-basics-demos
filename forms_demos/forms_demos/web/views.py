from django import forms
from django.shortcuts import render

from forms_demos.web.forms import PersonForm
from forms_demos.web.models import Person, Pet


def index_form(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:  # request.method == 'post':
        form = PersonForm(request.POST)
        if form.is_valid():
            '''
            `is_valid()`:
            - validates the form, returns `True` or `False`
            - fills `cleaned_data`
            '''
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('name', 'age')
        # exclude = ('pets', )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

        help_texts = {
            'name': 'Your name',
        }

        labels = {
            'age': 'The AGE',
        }


def index_model_form(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()  # same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            #
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }

    return render(request, 'model_forms.html', context)


def related_models_demo(request):
    pet = Pet.objects.get(pk=1)
    person = Person.objects.get(pk=1)
    # person.pets  # Person has `pets` field
    # pet.person_set  # Pet has no `person` field
    # print(list(pet.person_set.all()))
    print(list(pet.persons.all()))
    print(list(person.pets.all()))
