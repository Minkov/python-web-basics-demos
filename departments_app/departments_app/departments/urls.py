# `departments`'s app urls.py

from django.urls import path

from departments_app.departments.views import show_departments, show_department_details, redirect_to_first_department, \
    show_not_found

urlpatterns = (
    # /departments/
    path('', show_departments, name='show departments'),

    path('not-found/', show_not_found, name='not found'),

    path('redirect/', redirect_to_first_department, name='redirect demo'),

    # /departments/{department_id}/
    path('<department_id>/', show_department_details, name='show department details with string'),

    # /departments/int/{department_id}/
    path('by-id/<int:department_id>/', show_department_details, name='show department details'),
)

# paths = (
#     '',
#     '<department_id>/',
#     'int/<int:department_id>/',
# )
#
# urlpatterns = [path(url, sample_view) for url in paths]
#
# urlpatterns = ()
# urlpatterns += (path('', sample_view),)
# urlpatterns += (path('<department_id>/', sample_view),)
# urlpatterns += (path('int/<int:department_id>/', sample_view),)
