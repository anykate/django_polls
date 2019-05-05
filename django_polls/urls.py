from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    # Regular Django urls: https://chrisbartos.com/bonus-1-django-plus-angular-js/
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
]
