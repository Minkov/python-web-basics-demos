from django.urls import path

from django101.tasks.views import home

# App
urlpatterns = (
    path('', home),  # localhost:8001/
)
