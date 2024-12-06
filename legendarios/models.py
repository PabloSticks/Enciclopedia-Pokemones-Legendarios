from django.db import models

class Usuario(models.Model):
    ROLES = [
        ('admin', 'Admin'),
        ('visitante', 'Visitante'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=190, unique=True)
    rol = models.CharField(max_length=10, choices=ROLES, default='visitante')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class PokemonLegendario(models.Model):
    TIPOS = [
        ('agua', 'Agua'),
        ('fuego', 'Fuego'),
        ('planta', 'Planta'),
        ('eléctrico', 'Eléctrico'),
        ('psíquico', 'Psíquico'),
        # Agrega más tipos según sea necesario
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_1 = models.CharField(max_length=20, choices=TIPOS)
    tipo_2 = models.CharField(max_length=20, choices=TIPOS, blank=True, null=True)
    generación = models.CharField(max_length=50)
    estadísticas = models.JSONField()
    imagen = models.URLField()

    def __str__(self):
        return self.nombre
    
class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripción = models.TextField()

    def __str__(self):
        return self.nombre

class HabilidadLegendaria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return self.nombre

class EventoLegendario(models.Model):
    id = models.AutoField(primary_key=True)
    pokémon = models.ForeignKey(PokemonLegendario, on_delete=models.CASCADE, related_name='eventos')
    evento = models.CharField(max_length=200)
    descripción = models.TextField()
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return f"{self.evento} ({self.pokémon.nombre})"
