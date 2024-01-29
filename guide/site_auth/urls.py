from django.urls import path
from .views import CustomLoginView, CustomUserRegistrationView, CustomLogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomUserRegistrationView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name="logout")
]