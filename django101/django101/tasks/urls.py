'''
Do always when creating new Django App:

1. (Optional) Move to project directory
2. Create `urls.py` file
3. Register this Django app's `urls.py` in the project's `urls.py` file
4. Register this Django app in `settings.py`'s `INSTALLED_APPS`

'''
from django.urls import path

from .views import index

urlpatterns = (
    path("", index),
)
