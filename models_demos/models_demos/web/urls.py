from django.urls import path

from models_demos.web.views import index, delete_employee, department_details

urlpatterns = (
    path('', index, name='index'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
    # http://localhost:8000/departments/1/engineering/
    path('departments/<int:pk>/<slug:slug>/', department_details, name='details department'),
)
