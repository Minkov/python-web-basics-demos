# Project urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'departments/',
        include('departments_app.departments.urls')),
]
