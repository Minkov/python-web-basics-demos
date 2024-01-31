from django.shortcuts import render

from forms_advanced.web.forms import PersonForm, UpdatePersonForm, PersonFormSet
from forms_advanced.web.models import Person


def index(request):
    person_form = PersonForm()
    update_person_form = UpdatePersonForm()

    context = {
        "person_form": person_form,
        "update_person_form": update_person_form,
        "person_list": Person.objects.all(),
    }

    return render(request, "web/index.html", context)


def show_formset(request):
    form_set = PersonFormSet()
    context = {
        "form_set": form_set,
    }

    return render(request, "web/formsets.html", context)


def create_person(request):
    print(request.POST)
    form = PersonForm(request.POST, request.FILES, user=request.user)

    if form.is_valid():
        form.save()
