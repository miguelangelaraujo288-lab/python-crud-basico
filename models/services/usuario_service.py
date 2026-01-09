import json
from models.usuario import Usuario

RUTA_ARCHIVO = "data/usuarios.json"


def _leer_usuarios():
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def _guardar_usuarios(usuarios):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)


def crear_usuario(nombre, correo):
    usuarios = _leer_usuarios()
    nuevo_id = len(usuarios) + 1

    usuario = Usuario(nuevo_id, nombre, correo)
    usuarios.append(usuario.to_dict())

    _guardar_usuarios(usuarios)
    return usuario


def listar_usuarios():
    usuarios = _leer_usuarios()
    return [Usuario.from_dict(u) for u in usuarios]


def buscar_usuario_por_id(id_usuario):
    usuarios = _leer_usuarios()
    for u in usuarios:
        if u["id"] == id_usuario:
            return Usuario.from_dict(u)
    return None


def actualizar_usuario(id_usuario, nombre, correo):
    usuarios = _leer_usuarios()
    for u in usuarios:
        if u["id"] == id_usuario:
            u["nombre"] = nombre
            u["correo"] = correo
            _guardar_usuarios(usuarios)
            return Usuario.from_dict(u)
    return None


def eliminar_usuario(id_usuario):
    usuarios = _leer_usuarios()
    usuarios_filtrados = [u for u in usuarios if u["id"] != id_usuario]

    if len(usuarios) == len(usuarios_filtrados):
        return False

    _guardar_usuarios(usuarios_filtrados)
    return True

