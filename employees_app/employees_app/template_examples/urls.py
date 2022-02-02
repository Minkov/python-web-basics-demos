from django.urls import path

from employees_app.template_examples.views import index

urlpatterns = (
    path('', index, name='templates index'),
)
