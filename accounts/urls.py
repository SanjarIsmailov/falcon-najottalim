from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
]