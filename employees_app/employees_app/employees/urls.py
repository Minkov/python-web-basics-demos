from django.urls import path

from employees_app.employees.views import \
    list_departments, \
    department_details, not_found, create_department

urlpatterns = (
    path('create/', create_department),
    path('<str:id>/', department_details, name='department details'),  # departments/ID =>

    path('', list_departments, name='list departments'),
    # path('filter/by/<str:name>/order-by/<int:id>/', list_departments, name='custom url'),
    path('filter/by/order/', list_departments, name='custom url'),
    path('not-found/', not_found),
    # ^ localhost:8000/departments
    # path('create/', create_department),
    # path('update/', update_department),
    # path('delete/', delete_department),
)
