from django.urls import path

from form_basics.web.views import index, index_models, update_employee

urlpatterns = (
    path("", index, name="index"),
    path("modelforms/", index_models, name="index-models"),
    path("modelforms/<int:pk>/", update_employee, name="update-employee"),
)
