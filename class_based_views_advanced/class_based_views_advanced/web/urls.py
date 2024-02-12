from django.urls import path

from class_based_views_advanced.web.views import CreateTodoView, ListTodoView, DetailTodoView

urlpatterns = (
    # path("create/", create_todo),

    path("", ListTodoView.as_view(), name="todos-list"),

    path("create/", CreateTodoView.as_view(), name="todos-create"),

    path("<int:pk>/", DetailTodoView.as_view(), name="todos-detail"),
    path("<slug:slug>/", DetailTodoView.as_view(), name="todos-detail"),
    path("<int:pk>/<slug:slug>/", DetailTodoView.as_view(), name="todos-detail"),
)
