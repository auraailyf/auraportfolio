# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp.views import home_view # Import the new home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('', home_view, name='home'), # Add this line for the homepage
]