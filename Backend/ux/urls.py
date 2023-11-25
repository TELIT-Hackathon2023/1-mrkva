from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('telekomApp.urls')),  # Include your app's URLs
]