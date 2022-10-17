from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_part_2_demos.web.forms import TodoCreateForm, TodoForm, PersonCreateForm
from forms_part_2_demos.web.models import Person


def index(request):
    form_class = TodoForm

    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)

        if form.is_valid():
            # form.save()
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-persons.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list persons')

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)
