# django101.tasks.urls.py

from django.urls import path

from django101.tasks.views import show_bare_minimum_view, show_all_tasks, index

urlpatterns = (
    # http://localhost:8000/tasks/
    path('', index),
    # http://localhost:8000/tasks/it-works/
    path('it-works/', show_bare_minimum_view),
    # http://localhost:8000/tasks/all/
    path('all/', show_all_tasks),
    # localhost:8000/tasks/create/
    # path('create/', create),
)
