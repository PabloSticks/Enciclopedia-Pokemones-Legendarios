from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    ROLES = [
        ('Admin', 'Administrador'),
        ('Visitante', 'Visitante')
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    rol = models.CharField(max_length=10, choices=ROLES, default='Visitante')
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class HabilidadLegendaria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    pokemon = models.ForeignKey('PokemonLegendario', on_delete=models.CASCADE, related_name='habilidades')

    def __str__(self):
        return self.nombre

class PokemonLegendario(models.Model):
    TIPOS = [
        ('fuego', 'Fuego'),
        ('agua', 'Agua'),
        ('planta', 'Planta'),
        ('eléctrico', 'Eléctrico'),
        ('roca', 'Roca'),
        ('hielo', 'Hielo'),
        ('psíquico', 'Psíquico'),
        ('dragón', 'Dragón'),
        ('volador', 'Volador'),
        ('siniestro', 'Siniestro'),
        ('acero', 'Acero'),
        ('hada', 'Hada'),
        ('lucha', 'Lucha'),
        ('fantasma', 'Fantasma'),
        ('normal', 'Normal'),
        ('tierra', 'Tierra'),
        ('bicho', 'Bicho')
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_1 = models.CharField(max_length=15, choices=TIPOS)
    tipo_2 = models.CharField(max_length=15, choices=TIPOS, null=True, blank=True)
    generacion = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        if not self.tipo_1:
            raise ValidationError("El campo 'tipo_1' es obligatorio.")
        if self.generacion < 1 or self.generacion > 7:
            raise ValidationError("La generación debe estar entre 1 y 7.")

class EventoLegendario(models.Model):
    id = models.AutoField(primary_key=True)
    pokemon = models.ForeignKey(PokemonLegendario, on_delete=models.CASCADE)
    evento = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.evento} - {self.pokemon.nombre}"
