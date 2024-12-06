from django.urls import path
from .views import UsuarioListCreate, PokemonLegendarioList, EventoLegendarioListCreate

urlpatterns = [
    path('usuarios/', UsuarioListCreate.as_view(), name='usuarios'),
    path('legendarios/', PokemonLegendarioList.as_view(), name='legendarios'),
    path('eventos/', EventoLegendarioListCreate.as_view(), name='eventos'),
]
