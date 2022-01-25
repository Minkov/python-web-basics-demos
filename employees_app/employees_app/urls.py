from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home, go_to_home

# Mandatory, tuple or list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='index'),  # localhost:8000 -> home
    path('go-to-home/', go_to_home, name='go to home'),
    path('departments/', include('employees_app.employees.urls')),
]

'''
/my-view       (1)
/my-view/123   (2)
/my-view/123/4 (3)

GET /my-view/123/4 => (1)
'''
