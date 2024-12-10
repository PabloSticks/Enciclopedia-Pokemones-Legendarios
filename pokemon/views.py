from rest_framework import viewsets
from .models import Usuario, PokemonLegendario, Region, HabilidadLegendaria, EventoLegendario
from .serializers import UsuarioSerializer, PokemonLegendarioSerializer, RegionSerializer, HabilidadLegendariaSerializer, EventoLegendarioSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import admin_required
import requests
from django.http import HttpResponse, JsonResponse
import csv
import random

# API Views
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PokemonLegendarioViewSet(viewsets.ModelViewSet):
    queryset = PokemonLegendario.objects.select_related('region').all()
    serializer_class = PokemonLegendarioSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class HabilidadLegendariaViewSet(viewsets.ModelViewSet):
    queryset = HabilidadLegendaria.objects.all()
    serializer_class = HabilidadLegendariaSerializer

class EventoLegendarioViewSet(viewsets.ModelViewSet):
    queryset = EventoLegendario.objects.select_related('pokemon', 'region', 'usuario')
    serializer_class = EventoLegendarioSerializer

    def get_serializer_context(self):
        return {'request': self.request}



# views echas x mi

def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        try:
            usuario = Usuario.objects.get(correo=correo)
            request.session['usuario_id'] = usuario.id
            request.session['user_role'] = usuario.rol
            messages.success(request, f'Bienvenido, {usuario.nombre}!')
            return redirect('listar_pokemon')
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo no encontrado. Por favor, verifica tus datos.')
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    request.session.flush()
    return redirect('login')

def listar_eventos(request):
    response = requests.get('http://127.0.0.1:8000/api/eventos/')
    if response.status_code == 200:
        eventos = response.json()
    else:
        eventos = []

    user_role = request.session.get('user_role')
    
    for evento in eventos:
        if 'pokemon' in evento and 'region_nombre' in evento:
            evento['region'] = evento.get('region_nombre', 'Desconocida')

    return render(request, 'listar_eventos.html', {'eventos': eventos, 'user_role': user_role})


def listar_pokemones(request):
    nombre = request.GET.get('nombre', '')
    region = request.GET.get('region', '')
    tipo = request.GET.get('tipo', '')

    pokemones = PokemonLegendario.objects.all()

    if nombre:
        pokemones = pokemones.filter(nombre__icontains=nombre)
    if region:
        pokemones = pokemones.filter(region__nombre__icontains=region)
    if tipo:
        pokemones = pokemones.filter(tipo_1=tipo) | pokemones.filter(tipo_2=tipo)

    regiones = PokemonLegendario.objects.values_list('region__nombre', flat=True).distinct()
    regiones = [r for r in regiones if r]  # Filtrar valores None 
    tipos = [tipo[0] for tipo in PokemonLegendario.TIPOS]

    # Generar imágenes
    imagenes_destacadas = [
        "images/destacado_pokemon.jpg",
        "images/destacado_pokemon2.jpg",
        "images/destacado_pokemon3.jpg",
        "images/destacado_pokemon4.jpg",
        "images/destacado_pokemon5.jpg",
        "images/destacado_pokemon6.jpg",
        "images/destacado_pokemon7.jpg",
        "images/destacado_pokemon8.jpg",
        "images/destacado_pokemon9.jpg",
        "images/destacado_pokemon10.jpg",
        "images/destacado_pokemon11.jpg"
    ]

    # izquierda y derecha
    random.shuffle(imagenes_destacadas)
    imagenes_izquierda = imagenes_destacadas[:len(imagenes_destacadas)//2]
    imagenes_derecha = imagenes_destacadas[len(imagenes_destacadas)//2:]

    contexto = {
        'pokemones': pokemones,
        'regiones': regiones,
        'tipos': tipos,
        'imagenes_izquierda': imagenes_izquierda,
        'imagenes_derecha': imagenes_derecha,
    }

    return render(request, 'listar_pokemon.html', contexto)


def crear_eventos(request):
    if request.method == 'POST':
        data = {
            'evento': request.POST.get('evento'),
            'descripcion': request.POST.get('descripcion'),
            'fecha': request.POST.get('fecha'),
            'pokemon': int(request.POST.get('pokemon')),
            'region': int(request.POST.get('region')),
            'usuario': int(request.session.get('usuario_id')),
        }
        response = requests.post('http://127.0.0.1:8000/api/eventos/', json=data)

        if response.status_code == 201:
            messages.success(request, 'Evento creado exitosamente.')
            return redirect('listar_eventos')
        else:
            messages.error(request, f'Error al crear el evento: {response.text}')
            return redirect('crear_evento')

    pokemones = requests.get('http://127.0.0.1:8000/api/pokemon/').json()
    regiones = requests.get('http://127.0.0.1:8000/api/regiones/').json()
    return render(request, 'crear_evento.html', {'pokemones': pokemones, 'regiones': regiones})

@admin_required
def modificar_eventos(request, pk):
    if request.method == 'POST':
        data = {
            'evento': request.POST.get('evento'),
            'descripcion': request.POST.get('descripcion'),
            'fecha': request.POST.get('fecha'),
            'pokemon': int(request.POST.get('pokemon')),
            'region': int(request.POST.get('region')),
            'usuario': request.session.get('usuario_id')  
        }

        response = requests.put(f'http://127.0.0.1:8000/api/eventos/{pk}/', json=data)

        if response.status_code == 200:
            messages.success(request, 'Evento modificado exitosamente.')
            return redirect('listar_eventos')
        else:
            messages.error(request, f'Error al modificar el evento: {response.text}')
            return redirect('modificar_evento', pk=pk)

    evento = requests.get(f'http://127.0.0.1:8000/api/eventos/{pk}/').json()
    pokemones = requests.get('http://127.0.0.1:8000/api/pokemon/').json()
    regiones = requests.get('http://127.0.0.1:8000/api/regiones/').json()
    return render(request, 'modificar_evento.html', {
        'evento': evento,
        'pokemones': pokemones,
        'regiones': regiones
    })



@admin_required
def eliminar_eventos(request, pk):
    if request.method == 'POST':
        response = requests.delete(f'http://127.0.0.1:8000/api/eventos/{pk}/')
        if response.status_code == 204:
            messages.success(request, 'Evento eliminado exitosamente.')
            return redirect('listar_eventos')
        else:
            messages.error(request, 'Error al eliminar el evento.')
            return redirect('eliminar_evento', pk=pk)

    evento = requests.get(f'http://127.0.0.1:8000/api/eventos/{pk}/').json()
    return render(request, 'eliminar_evento.html', {'evento': evento})

def listar_eventos(request):
    eventos = requests.get('http://127.0.0.1:8000/api/eventos/').json()
    user_role = request.session.get('user_role')
    return render(request, 'listar_eventos.html', {'eventos': eventos, 'user_role': user_role})



def listarhabilidades_legendarias(request):
    nombre = request.GET.get('nombre', '')
    region = request.GET.get('region', '')
    tipo = request.GET.get('tipo', '')

    pokemones = PokemonLegendario.objects.prefetch_related('habilidades').all()

    if nombre:
        pokemones = pokemones.filter(nombre__icontains=nombre)
    if region:
        pokemones = pokemones.filter(region__nombre__icontains=region)
    if tipo:
        pokemones = pokemones.filter(tipo_1=tipo) | pokemones.filter(tipo_2=tipo)

    regiones = PokemonLegendario.objects.values_list('region__nombre', flat=True).distinct()
    regiones = [r for r in regiones if r]  # Filtrar valores None 

    tipos = [tipo[0] for tipo in PokemonLegendario.TIPOS]

    context = {
        'pokemones': pokemones,
        'regiones': regiones,
        'tipos': tipos,
    }

    return render(request, 'habilidad_pokemon.html', context)


def combinar_datos(request):
    evento = request.GET.get('evento', '')
    pokemon = request.GET.get('pokemon', '')
    region = request.GET.get('region', '')
    usuario = request.GET.get('usuario', '')

    eventos = EventoLegendario.objects.select_related('pokemon', 'region', 'usuario').all()

    if evento:
        eventos = eventos.filter(evento__icontains=evento)
    if pokemon:
        eventos = eventos.filter(pokemon__nombre__icontains=pokemon)
    if region:
        eventos = eventos.filter(region__nombre__icontains=region)
    if usuario:
        eventos = eventos.filter(usuario__nombre__icontains=usuario)

    # Si el usuario selecciona descargar CSV
    if 'descargar' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ListadoFiltros.csv"'

        writer = csv.writer(response)
        writer.writerow(['Evento', 'Descripción', 'Fecha', 'Pokémon', 'Región', 'Usuario'])
        for evento in eventos:
            writer.writerow([
                evento.evento,
                evento.descripcion,
                evento.fecha,
                evento.pokemon.nombre,
                evento.region.nombre,
                evento.usuario.nombre
            ])

        return response

    return render(request, 'combinar_datos.html', {'eventos': eventos})

def exportar_csv(request):
    eventos = EventoLegendario.objects.select_related('pokemon', 'region', 'usuario')

    filtro_region = request.GET.get('region', None)
    filtro_pokemon = request.GET.get('pokemon', None)
    filtro_usuario = request.GET.get('usuario', None)

    if filtro_region:
        eventos = eventos.filter(region__nombre__icontains=filtro_region)
    if filtro_pokemon:
        eventos = eventos.filter(pokemon__nombre__icontains=filtro_pokemon)
    if filtro_usuario:
        eventos = eventos.filter(usuario__nombre__icontains=filtro_usuario)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos_combinados.csv"'

    writer = csv.writer(response)
    writer.writerow(['Evento', 'Descripción', 'Fecha', 'Pokémon', 'Región', 'Usuario', 'Habilidades'])

    for evento in eventos:
        habilidades = HabilidadLegendaria.objects.filter(pokemon=evento.pokemon)
        habilidades_lista = ", ".join([habilidad.nombre for habilidad in habilidades])
        writer.writerow([
            evento.evento,
            evento.descripcion,
            evento.fecha,
            evento.pokemon.nombre,
            evento.region.nombre,
            evento.usuario.nombre,
            habilidades_lista
        ])

    return response

