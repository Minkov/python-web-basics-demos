import time

from django import http
from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Task

"""
# FBV:
1. A function that has one or more params
2. Returns a response
"""


#
# def index(request):
#     name = request.GET.get("name", "NONAME")
#
#     content = "<h1>It works!</h1>" + \
#               f"<p>You are welcome to my project, {name}!</p>" + \
#               "<ul><li>1</li><li>2</li></ul>"
#
#     return http.HttpResponse(content)
#
#     # headers={
#     #     "Content-Type": "application/json",
#     # }

# def index(request):
#     title_filter = request.GET.get("filter", None)
#     tasks = Task.objects.all()
#
#     if title_filter:
#         tasks = tasks.filter(title__icontains=title_filter.lower())
#
#     if not tasks:
#         return HttpResponse("<h1>No tasks!!!</h1>")
#
#     result = []
#
#     for task in tasks:
#         result.append(f"""
# <li>
#     <h2>{task.title}</h2>
#     <p>{task.description}</p>
# </li>
#         """)
#
#     ul = f"<ul>{''.join(result)}</ul>"
#
#     content = f"""
#     <h1>{len(tasks)} Tasks</h1>
#     {ul}
#     """
#     return HttpResponse(content)

def index(request):
    title_filter = request.GET.get("title_filter", "")
    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    context = {
        "title": "The tasks app!!!",
        "task_list": tasks,
        "task_list_count": tasks.count(),
        "title_filter": title_filter,
    }

    return render(
        request,
        "tasks/index.html",
        context,
    )
