from django.urls import path

from forms_part_2_demos.web.views import index, list_persons, create_person

urlpatterns = [
    path('', index, name='index'),
    path('persons/', list_persons, name='list persons'),
    path('persons/create/', create_person, name='create person'),
]
