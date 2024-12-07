from django.urls import path

from .views import (
    UsuarioViewSet, PokemonLegendarioViewSet, RegionViewSet,
    HabilidadLegendariaViewSet, EventoLegendarioViewSet, listar_pokemon, crear_pokemon
)

# Mapeo de métodos HTTP a los métodos del ViewSet
urlpatterns = [
    # API REST
    path('api/usuarios/', UsuarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='usuario-list'),
    path('api/usuarios/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='usuario-detail'),

    path('api/pokemon/', PokemonLegendarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='pokemon-list'),
    path('api/pokemon/<int:pk>/', PokemonLegendarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='pokemon-detail'),

    path('api/regiones/', RegionViewSet.as_view({'get': 'list', 'post': 'create'}), name='region-list'),
    path('api/regiones/<int:pk>/', RegionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='region-detail'),

    path('api/habilidades/', HabilidadLegendariaViewSet.as_view({'get': 'list', 'post': 'create'}), name='habilidad-list'),
    path('api/habilidades/<int:pk>/', HabilidadLegendariaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='habilidad-detail'),

    path('api/eventos/', EventoLegendarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='evento-list'),
    path('api/eventos/<int:pk>/', EventoLegendarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='evento-detail'),

    # Vistas HTML
    path('listar', listar_pokemon, name='listar_pokemon'), 
    path('crear/', crear_pokemon, name='crear_pokemon'),  
] 

