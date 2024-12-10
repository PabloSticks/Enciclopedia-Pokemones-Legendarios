from rest_framework import serializers
from .models import Usuario, PokemonLegendario, Region, HabilidadLegendaria, EventoLegendario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PokemonLegendarioSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()
    region_nombre = serializers.CharField(source='region.nombre', read_only=True)
    
    class Meta:
        model = PokemonLegendario
        fields = ['id', 'nombre', 'tipo_1', 'tipo_2', 'generacion', 'descripcion', 'region', 'region_nombre', 'imagen']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class HabilidadLegendariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadLegendaria
        fields = '__all__'

class EventoLegendarioSerializer(serializers.ModelSerializer):
    pokemon_nombre = serializers.CharField(source='pokemon.nombre', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)
    region_nombre = serializers.CharField(source='region.nombre', read_only=True)  

    class Meta:
        model = EventoLegendario
        fields = [
            'id', 'evento', 'descripcion', 'fecha', 'pokemon', 'usuario',
            'pokemon_nombre', 'usuario_nombre', 'region', 'region_nombre'
        ]
