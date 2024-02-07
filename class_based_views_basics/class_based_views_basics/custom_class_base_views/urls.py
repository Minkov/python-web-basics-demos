from django.urls import path

from class_based_views_basics.custom_class_base_views.views import index, IndexView

urlpatterns = (
    path("", index, name='ccbc_index'),
    path("cbv/", IndexView.as_view(), name='ccbc_cbv_index'),
)