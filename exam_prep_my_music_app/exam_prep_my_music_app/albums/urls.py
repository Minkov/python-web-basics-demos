from django.urls import path, include

from exam_prep_my_music_app.albums.views import CreateAlbumView, DetailAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = (
    path("add/", CreateAlbumView.as_view(), name="create_album"),
    path(
        "<int:pk>/",
        include([
            path("details/", DetailAlbumView.as_view(), name="details_album"),
            path("edit/", EditAlbumView.as_view(), name="edit_album"),
            path("delete/", DeleteAlbumView.as_view(), name="delete_album"),
        ])
    )
)
