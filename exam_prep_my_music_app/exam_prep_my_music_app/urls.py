from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include('exam_prep_my_music_app.web.urls')),
    path("album/", include('exam_prep_my_music_app.albums.urls')),
    path("profile/", include('exam_prep_my_music_app.profiles.urls')),
]
