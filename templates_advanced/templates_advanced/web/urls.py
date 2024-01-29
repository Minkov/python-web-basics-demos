from django.urls import path

from templates_advanced.web.views import index, about, show_bootstrap

urlpatterns = (
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("bootstrap/", show_bootstrap, name="show_bootstrap"),
)
