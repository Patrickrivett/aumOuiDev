from django.urls import path
from .views import RegisterView, EmailTokenObtainPairView, ProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('jwt/create/', EmailTokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
