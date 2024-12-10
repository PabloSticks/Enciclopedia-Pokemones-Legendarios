import requests

BASE_URL = "http://127.0.0.1:8000/api/pokemon/"
BASE_REGION_URL = "http://127.0.0.1:8000/api/regiones/"

def listar_regiones():
    """Lista todas las regiones disponibles."""
    response = requests.get(BASE_REGION_URL)
    if response.status_code == 200:
        regiones = response.json()
        print("\n=== Lista de Regiones ===")
        for region in regiones:
            print(f"{region['id']}: {region['nombre']}")
        return regiones
    else:
        print("Error al obtener las regiones.")
        return []

def crear_pokemon():
    """Crea un nuevo Pokémon solicitando todos los datos."""
    print("\n=== Crear un nuevo Pokémon ===")
    nombre = input("Nombre del Pokémon: ")
    tipo_1 = input("Tipo 1: ").lower()  # Convertir a minúsculas
    tipo_2 = input("Tipo 2 (Deja vacío si no aplica): ").lower() or None  # Convertir a minúsculas si aplica
    generacion = int(input("Generación: "))
    descripcion = input("Descripción: ")

    # Mostrar lista de regiones para que el usuario elija
    regiones = listar_regiones()
    if not regiones:
        print("No hay regiones disponibles. Cancela la operación.")
        return

    region_nombre = input("Nombre de la Región: ").capitalize()
    region = next((region for region in regiones if region["nombre"] == region_nombre), None)
    if not region:
        print(f"La región '{region_nombre}' no existe.")
        return

    imagen_ruta = input("Ruta de la imagen (Deja vacío si no aplica): ")

    # Enviar datos a la API
    with open(imagen_ruta, 'rb') if imagen_ruta else None as imagen_file:
        files = {"imagen": imagen_file} if imagen_file else None
        data = {
            "nombre": nombre,
            "tipo_1": tipo_1,  # En minúsculas
            "tipo_2": tipo_2,  # En minúsculas
            "generacion": generacion,
            "descripcion": descripcion,
            "region": region["id"],
        }
        response = requests.post(BASE_URL, data=data, files=files)

    if response.status_code == 201:
        print(f"Pokémon '{nombre}' creado exitosamente.")
    else:
        print(f"Error al crear el Pokémon: {response.json()}")

        
def listar_pokemones():
    """Lista todos los Pokémon."""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        pokemones = response.json()
        print(f"\n{'ID':<5}{'Nombre':<20}{'Tipo 1':<10}{'Tipo 2':<10}{'Generación':<10}{'Región':<15}{'Imagen':<10}")
        print("-" * 80)
        for pokemon in pokemones:
            print(
                f"{pokemon['id']:<5}{pokemon['nombre']:<20}{pokemon['tipo_1']:<10}"
                f"{pokemon['tipo_2'] or 'N/A':<10}{pokemon['generacion']:<10}"
                f"{pokemon.get('region_nombre', 'N/A'):<15}{pokemon.get('imagen', 'N/A'):<10}"
            )
    else:
        print("Error al obtener la lista de Pokémon.")

def actualizar_pokemon():
    """Modifica un Pokémon existente."""
    pokemon_id = int(input("\nID del Pokémon a modificar: "))
    response = requests.get(f"{BASE_URL}{pokemon_id}/")
    if response.status_code != 200:
        print("El Pokémon especificado no existe.")
        return

    pokemon = response.json()
    print(f"\nEditando Pokémon: {pokemon['nombre']}")

    nombre = input(f"Nuevo nombre [{pokemon['nombre']}]: ") or pokemon['nombre']
    tipo_1 = input(f"Nuevo Tipo 1 [{pokemon['tipo_1']}]: ") or pokemon['tipo_1']
    tipo_2 = input(f"Nuevo Tipo 2 [{pokemon['tipo_2'] or 'N/A'}]: ") or pokemon['tipo_2']
    generacion = int(input(f"Nueva Generación [{pokemon['generacion']}]: ") or pokemon['generacion'])
    descripcion = input(f"Nueva Descripción [{pokemon['descripcion']}]: ") or pokemon['descripcion']

    # Validar la región
    regiones = listar_regiones()
    if not regiones:
        print("No hay regiones disponibles. Cancela la operación.")
        return

    region_nombre = input(f"Nueva Región [{pokemon.get('region_nombre', 'N/A')}]: ").capitalize()
    region = next((region for region in regiones if region["nombre"] == region_nombre), None)
    if not region:
        print(f"La región '{region_nombre}' no existe.")
        return

    imagen_ruta = input("Ruta de la nueva imagen (Deja vacío si no aplica): ")

    # Enviar datos actualizados a la API
    with open(imagen_ruta, 'rb') if imagen_ruta else None as imagen_file:
        files = {"imagen": imagen_file} if imagen_file else None
        data = {
            "nombre": nombre,
            "tipo_1": tipo_1,
            "tipo_2": tipo_2,
            "generacion": generacion,
            "descripcion": descripcion,
            "region": region["id"],
        }
        response = requests.put(f"{BASE_URL}{pokemon_id}/", data=data, files=files)

    if response.status_code == 200:
        print(f"Pokémon '{nombre}' modificado exitosamente.")
    else:
        print(f"Error al modificar el Pokémon: {response.json()}")

def eliminar_pokemon():
    """Elimina un Pokémon."""
    pokemon_id = int(input("\nID del Pokémon a eliminar: "))
    response = requests.get(f"{BASE_URL}{pokemon_id}/")
    if response.status_code != 200:
        print("El Pokémon especificado no existe.")
        return

    confirmacion = input(f"¿Estás seguro de que deseas eliminar '{response.json()['nombre']}'? (s/n): ")
    if confirmacion.lower() == 's':
        response = requests.delete(f"{BASE_URL}{pokemon_id}/")
        if response.status_code == 204:
            print("Pokémon eliminado exitosamente.")
        else:
            print("Error al eliminar el Pokémon.")
    else:
        print("Operación cancelada.")

def menu():
    """Muestra el menú de opciones."""
    while True:
        print("\n=== Gestión de Pokémon Legendarios ===")
        print("1. Crear Pokémon")
        print("2. Listar Pokémon")
        print("3. Modificar Pokémon")
        print("4. Eliminar Pokémon")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_pokemon()
        elif opcion == "2":
            listar_pokemones()
        elif opcion == "3":
            actualizar_pokemon()
        elif opcion == "4":
            eliminar_pokemon()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()
