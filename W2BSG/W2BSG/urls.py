from django.urls import path
from login import views

urlpatterns = [
    path('register', views.register_user),
    path('login', views.login),
]
