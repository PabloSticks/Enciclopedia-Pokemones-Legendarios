from rest_framework import generics
from .models import Usuario, PokemonLegendario, Region, HabilidadLegendaria, EventoLegendario
from .serializers import UsuarioSerializer, PokemonLegendarioSerializer, RegionSerializer, HabilidadLegendariaSerializer, EventoLegendarioSerializer

# Listar y Crear Usuarios
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Listar Pokémon Legendarios
class PokemonLegendarioList(generics.ListAPIView):
    queryset = PokemonLegendario.objects.all()
    serializer_class = PokemonLegendarioSerializer

# Listar y Crear Eventos Legendarios
class EventoLegendarioListCreate(generics.ListCreateAPIView):
    queryset = EventoLegendario.objects.all()
    serializer_class = EventoLegendarioSerializer
