from django.urls import path, reverse

from urls_and_views_demos.departments.views import department_details, department_details_by_name

urlpatterns = (
    # path("departments/1/", department_1_details),
    # path("departments/2/", department_2_details),
    path("<int:pk>/", department_details, name='department_details'),  # departments/<int:pk>/
    path("<str:name>/", department_details_by_name),
)