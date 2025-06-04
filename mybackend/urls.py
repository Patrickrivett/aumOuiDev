from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  # Your custom auth endpoints
    path('auth/', include('djoser.urls')),    # Djoser's other endpoints (password reset, etc.)
]
