from django.urls import path
from .views import (
    RegisterView,
    MyTokenObtainPairView,
    ProfileView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/',        RegisterView.as_view(),         name='signup'),
    path('login/',         MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(),     name='token_refresh'),
    path('profile/',       ProfileView.as_view(),          name='profile'),
]
