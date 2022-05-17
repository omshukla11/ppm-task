from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='Signup'),
    path('login/', Login.as_view(), name="Login"),
    path('token-refresh/',TokenRefreshView.as_view(),name="RefreshToken"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]