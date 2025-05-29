from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser’s endpoints:
    path('auth/', include('djoser.urls')),        # signup, users/me, password reset, etc.
    path('auth/', include('djoser.urls.jwt')),    # /jwt/create/, /jwt/refresh/, /jwt/verify/
]
