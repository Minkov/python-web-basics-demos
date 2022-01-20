from django.contrib import admin
from django.urls import path, include
# Project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django101.tasks.urls')),
]
