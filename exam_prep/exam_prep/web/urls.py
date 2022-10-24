from django.urls import path, include

from exam_prep.web.views import index, \
    details_album, add_album, edit_album, delete_album, \
    details_profile, delete_profile, add_profile

urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('details/<int:pk>/', details_album, name='details album'),
        path('add/', add_album, name='add album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
