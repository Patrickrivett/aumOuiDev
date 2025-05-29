from django.contrib import admin
from django.urls import path, include
# import the Simple JWT views:
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # your own endpoints (e.g. profile, custom auth, etc.)
    path('api/auth/', include('accounts.urls')),

    # Djoser handles signup/password-reset/etc
    path('auth/', include('djoser.urls')),

    # instead of `include('djoser.urls.jwt')`, use the Simple JWT views:
    path(
        'auth/jwt/create/',
        TokenObtainPairView.as_view(),
        name='jwt-create'
    ),
    path(
        'auth/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='jwt-refresh'
    ),
    path(
        'auth/jwt/verify/',
        TokenVerifyView.as_view(),
        name='jwt-verify'
    ),
]
