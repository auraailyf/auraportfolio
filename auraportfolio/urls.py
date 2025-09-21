# auraportfolio/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp.views import home_view  # Make sure this import exists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # This path handles the home page (e.g., yoursite.com/)
    path('api/contact/', include('myapp.urls')), # This path handles the API endpoint
]