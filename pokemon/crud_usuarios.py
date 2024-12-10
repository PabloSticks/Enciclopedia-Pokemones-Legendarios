import requests

BASE_URL = "http://127.0.0.1:8000/api/usuarios/"


def crear_usuario():
    """Crear un nuevo usuario."""
    print("\n=== Crear Usuario ===")
    nombre = input("Nombre del usuario: ")
    correo = input("Correo electrónico: ")
    rol = input("Rol (Admin/Visitante): ").capitalize()

    if rol not in ['Admin', 'Visitante']:
        print("Rol inválido. Debe ser 'Admin' o 'Visitante'.")
        return

    data = {
        "nombre": nombre,
        "correo": correo,
        "rol": rol
    }

    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print(f"Usuario '{nombre}' creado exitosamente.")
    else:
        print(f"Error al crear el usuario: {response.json()}")


def listar_usuarios():
    """Listar todos los usuarios."""
    print("\n=== Listar Usuarios ===")
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        usuarios = response.json()
        print(f"{'ID':<5}{'Nombre':<20}{'Correo':<30}{'Rol':<15}{'Fecha Registro':<15}")
        print("-" * 80)
        for usuario in usuarios:
            print(f"{usuario['id']:<5}{usuario['nombre']:<20}{usuario['correo']:<30}{usuario['rol']:<15}{usuario['fecha_registro']:<15}")
    else:
        print("Error al obtener la lista de usuarios.")


def actualizar_usuario():
    """Actualizar un usuario existente."""
    print("\n=== Actualizar Usuario ===")
    usuario_id = input("ID del usuario a actualizar: ")

    response = requests.get(f"{BASE_URL}{usuario_id}/")
    if response.status_code != 200:
        print("El usuario especificado no existe.")
        return

    usuario = response.json()
    print(f"Editando Usuario: {usuario['nombre']}")

    nombre = input(f"Nuevo nombre [{usuario['nombre']}]: ") or usuario['nombre']
    correo = input(f"Nuevo correo electrónico [{usuario['correo']}]: ") or usuario['correo']
    rol = input(f"Nuevo rol (Admin/Visitante) [{usuario['rol']}]: ").capitalize() or usuario['rol']

    if rol not in ['Admin', 'Visitante']:
        print("Rol inválido. Debe ser 'Admin' o 'Visitante'.")
        return

    data = {
        "nombre": nombre,
        "correo": correo,
        "rol": rol
    }

    response = requests.put(f"{BASE_URL}{usuario_id}/", json=data)
    if response.status_code == 200:
        print(f"Usuario '{nombre}' actualizado exitosamente.")
    else:
        print(f"Error al actualizar el usuario: {response.json()}")


def eliminar_usuario():
    """Eliminar un usuario."""
    print("\n=== Eliminar Usuario ===")
    usuario_id = input("ID del usuario a eliminar: ")

    response = requests.get(f"{BASE_URL}{usuario_id}/")
    if response.status_code != 200:
        print("El usuario especificado no existe.")
        return

    confirmacion = input(f"¿Estás seguro de que deseas eliminar '{response.json()['nombre']}'? (s/n): ").lower()
    if confirmacion == 's':
        response = requests.delete(f"{BASE_URL}{usuario_id}/")
        if response.status_code == 204:
            print("Usuario eliminado exitosamente.")
        else:
            print("Error al eliminar el usuario.")
    else:
        print("Operación cancelada.")


def menu():
    """Menú principal."""
    while True:
        print("\n=== Gestión de Usuarios ===")
        print("1. Crear Usuario")
        print("2. Listar Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
