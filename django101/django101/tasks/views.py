from django import http
from django.shortcuts import render

from django101.tasks.models import Task
from django101.tasks.tasks_utils import get_all_tasks


# django101.tasks.views.py

def show_bare_minimum_view(request):
    return http.HttpResponse('It works')


def show_all_tasks(request):
    all_tasks = get_all_tasks()
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)


    return http.HttpResponse(result)


def index(request):
    all_tasks = get_all_tasks()

    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }

    return render(request, 'index.html', context)
