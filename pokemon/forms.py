from django import forms
from .models import PokemonLegendario

class PokemonForm(forms.ModelForm):
    class Meta:
        model = PokemonLegendario
        fields = ['nombre', 'tipo_1', 'tipo_2', 'generacion', 'descripcion', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }