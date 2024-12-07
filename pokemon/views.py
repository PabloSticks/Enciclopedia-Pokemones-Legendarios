from rest_framework import viewsets
from .models import Usuario, PokemonLegendario, Region, HabilidadLegendaria, EventoLegendario
from .serializers import UsuarioSerializer, PokemonLegendarioSerializer, RegionSerializer, HabilidadLegendariaSerializer, EventoLegendarioSerializer
from django.shortcuts import render, redirect
from .models import PokemonLegendario
from .forms import PokemonForm

# INICIO VISTAS API

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PokemonLegendarioViewSet(viewsets.ModelViewSet):
    queryset = PokemonLegendario.objects.all()
    serializer_class = PokemonLegendarioSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class HabilidadLegendariaViewSet(viewsets.ModelViewSet):
    queryset = HabilidadLegendaria.objects.all()
    serializer_class = HabilidadLegendariaSerializer

class EventoLegendarioViewSet(viewsets.ModelViewSet):
    queryset = EventoLegendario.objects.all()
    serializer_class = EventoLegendarioSerializer

# FIN VISTAS API


def listar_pokemon(request):
    pokemones = PokemonLegendario.objects.all()
    return render(request, 'pokemon/listar_pokemon.html', {'pokemones': pokemones})

def crear_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)  # Agregamos request.FILES para manejar archivos
        if form.is_valid():
            form.save()  # Esto guardará la imagen junto con el resto de los datos
            return redirect('listar_pokemon')
    else:
        form = PokemonForm()
    return render(request, 'pokemon/registrar_pokemon.html', {'form': form})
