from rest_framework import serializers
from .models import Usuario, PokemonLegendario, Region, HabilidadLegendaria, EventoLegendario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PokemonLegendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonLegendario
        fields = ['id', 'nombre', 'tipo_1', 'tipo_2', 'generacion', 'descripcion', 'imagen']
        
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class HabilidadLegendariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadLegendaria
        fields = '__all__'

class EventoLegendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoLegendario
        fields = '__all__'

