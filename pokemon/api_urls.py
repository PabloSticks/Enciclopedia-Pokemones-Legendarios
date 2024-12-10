from django.urls import path
from .views import (
    UsuarioViewSet, PokemonLegendarioViewSet, RegionViewSet,
    HabilidadLegendariaViewSet, EventoLegendarioViewSet
)

urlpatterns = [
    path('usuarios/', UsuarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='usuario-detail'),

    path('pokemon/', PokemonLegendarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='pokemon-list'),
    path('pokemon/<int:pk>/', PokemonLegendarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='pokemon-detail'),

    path('regiones/', RegionViewSet.as_view({'get': 'list', 'post': 'create'}), name='region-list'),
    path('regiones/<int:pk>/', RegionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='region-detail'),

    path('habilidades/', HabilidadLegendariaViewSet.as_view({'get': 'list', 'post': 'create'}), name='habilidad-list'),
    path('habilidades/<int:pk>/', HabilidadLegendariaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='habilidad-detail'),

    path('eventos/', EventoLegendarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='evento-list'),
    path('eventos/<int:pk>/', EventoLegendarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='evento-detail'),
]
