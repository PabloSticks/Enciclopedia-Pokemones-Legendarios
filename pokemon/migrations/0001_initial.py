# Generated by Django 5.1.1 on 2024-12-07 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HabilidadLegendaria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PokemonLegendario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_1', models.CharField(choices=[('fuego', 'Fuego'), ('agua', 'Agua'), ('planta', 'Planta'), ('eléctrico', 'Eléctrico'), ('roca', 'Roca'), ('hielo', 'Hielo'), ('psíquico', 'Psíquico'), ('dragón', 'Dragón'), ('volador', 'Volador'), ('siniestro', 'Siniestro'), ('acero', 'Acero'), ('hada', 'Hada'), ('lucha', 'Lucha'), ('fantasma', 'Fantasma'), ('normal', 'Normal'), ('tierra', 'Tierra'), ('bicho', 'Bicho')], max_length=15)),
                ('tipo_2', models.CharField(blank=True, choices=[('fuego', 'Fuego'), ('agua', 'Agua'), ('planta', 'Planta'), ('eléctrico', 'Eléctrico'), ('roca', 'Roca'), ('hielo', 'Hielo'), ('psíquico', 'Psíquico'), ('dragón', 'Dragón'), ('volador', 'Volador'), ('siniestro', 'Siniestro'), ('acero', 'Acero'), ('hada', 'Hada'), ('lucha', 'Lucha'), ('fantasma', 'Fantasma'), ('normal', 'Normal'), ('tierra', 'Tierra'), ('bicho', 'Bicho')], max_length=15, null=True)),
                ('generacion', models.IntegerField()),
                ('descripcion', models.JSONField()),
                ('imagen', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('rol', models.CharField(choices=[('Admin', 'Administrador'), ('Visitante', 'Visitante')], default='Visitante', max_length=10)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('puntos', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventoLegendario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('evento', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemonlegendario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.usuario')),
            ],
        ),
    ]
