from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('templates_demos.web.urls')),
]

'''
Create django app

1. Add to `installed_apps`
2. Create urls.py in the app
3. Include app's urls.py in the project's urs.py

'''
