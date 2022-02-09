from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home

# Mandatory, tuple or list
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='index'),  # localhost:8000 -> home
                  path('employees/', include('employees_app.employees.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
