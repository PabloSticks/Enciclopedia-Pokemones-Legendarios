from django.db import models

from django.db import models

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
    puntos = models.IntegerField(null=True, blank=True, default=0)

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
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)  # Configuración para subir imágenes


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

    def __str__(self):
        return self.nombre

class EventoLegendario(models.Model):
    id = models.AutoField(primary_key=True)
    pokemon = models.ForeignKey(PokemonLegendario, on_delete=models.CASCADE)
    evento = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.evento} - {self.pokemon.nombre}"
