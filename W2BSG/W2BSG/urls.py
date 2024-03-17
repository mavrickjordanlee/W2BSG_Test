from django.urls import path, include
from login import views

urlpatterns = [
    path('register', views.register_user),
    path('login', views.login),
    path('games', include('games.urls'))
]
