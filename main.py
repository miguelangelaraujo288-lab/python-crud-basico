from models.services.usuario_service import (
    crear_usuario,
    listar_usuarios,
    actualizar_usuario,
    eliminar_usuario
)

def menu():
    print("\n=== MENÚ CRUD DE USUARIOS ===")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        crear_usuario(nombre, correo)
        print("✅ Usuario creado")

    elif opcion == "2":
        usuarios = listar_usuarios()
        for u in usuarios:
            print(f"{u['id']} - {u['nombre']} - {u['correo']}")

    elif opcion == "3":
        id_usuario = int(input("ID del usuario: "))
        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo: ")
        actualizar_usuario(id_usuario, nombre, correo)
        print("✏️ Usuario actualizado")

    elif opcion == "4":
        id_usuario = int(input("ID del usuario: "))
        eliminar_usuario(id_usuario)
        print("🗑️ Usuario eliminado")

    elif opcion == "5":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("❌ Opción inválida")

