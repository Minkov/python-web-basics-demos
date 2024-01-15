from django.urls import path, include

from urls_and_views_demos.core.views import index, index_json, redirect_to_softuni, redirect_to_index, \
    redirect_to_index_with_params, raise_error, raise_exception

urlpatterns = (
    # redirects
    path('to-softuni/', redirect_to_softuni),
    path('to-index/', redirect_to_index, name='redirect_to_index'),
    path('to-index-with-params/', redirect_to_index_with_params, name='redirect_to_index_with_params'),

    # Errors
    path('raise_error/', raise_error, name='raise_error_with_response'),
    path('raise_exception/', raise_exception, name='raise_exception'),

    # Normal URLs
    path('', index, name='index_no_params'),
    path('<int:pk>/', index),
    path('<slug:slug>/', index),
    path('<int:pk>/<slug:slug>/', index, name='index_with_pk_and_slug'),

    path('json/', include(
        [
            path('', index_json),
            path('<int:pk>/', index_json),
            path('<slug:slug>/', index_json),
            path('<int:pk>/<slug:slug>/', index_json)
        ])),
)
