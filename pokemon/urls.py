from django.urls import path, include
from .views import (login_view, listar_pokemones, listar_eventos, crear_eventos, modificar_eventos, 
    eliminar_eventos, logout_view, listarhabilidades_legendarias, combinar_datos, exportar_csv)

urlpatterns = [
    path('', login_view, name='login'),  
    path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'),
    path('listar_pokemon/', listar_pokemones, name='listar_pokemon'),
    path('listar_eventos/', listar_eventos, name='listar_eventos'),
    path('crear_evento/', crear_eventos, name='crear_evento'),

    path('modificar_evento/<int:pk>/', modificar_eventos, name='modificar_evento'),
    path('eliminar_evento/<int:pk>/', eliminar_eventos, name='eliminar_evento'),

    path('habilidades_legendarias/', listarhabilidades_legendarias, name='habilidades_legendarias'),

    path('combinar_datos/', combinar_datos, name='combinar_datos'),
    path('exportar_csv/', exportar_csv, name='exportar_csv'),



    path('api/', include('pokemon.api_urls'))
]