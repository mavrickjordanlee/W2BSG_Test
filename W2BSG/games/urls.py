from django.urls import path
from .views import *

urlpatterns = [
    path('', games_list),
    path('search/<str:game_name>', search_game, name='game-search'),
    path('<str:_id>', get_game_details, name='game-details'),
]