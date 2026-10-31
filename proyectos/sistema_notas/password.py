import hashlib

aUsuarios = [

    "Administrador",
    "Docente",
    "Coordinador_Academico",
    "Director_Carrera",
    "Secretaria_Academica"
]
# Hashes generados previamente (corresponden a las contraseñas reales)
aContrasenasHash = [
    "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",  # Hash de "1234"
    "f8638b979b2f4f793ddb6dbd197e0ee25a7a6ea32b0ae22f5e3c5d119d839e75",  # Hash de "5678"
    "13b1475cbe243903914ceaa33c2335db2d7e0c23c79e0df8a0da7d8d311944ee",  # Hash de "5523"
    "a1fb4e703a9ef1fa4936801721ff285a97ac85330856674412e054892afe6972",  # Hash de "2468"
    "8cce10345c5e1de90d277b9869465f5972b828afbbbfd7ef08b1d835eedee993"   # Hash de "9012"
]

def fGenerarHash(sContrasena):
    return hashlib.sha256(
        str(sContrasena).encode("utf-8")
    ).hexdigest()

def fVerificarCredenciales(sUsuario, sContrasena):
    if sUsuario in aUsuarios:
        nPosicion = aUsuarios.index(sUsuario)
        sHashIngresado = fGenerarHash(sContrasena)
        if sHashIngresado == aContrasenasHash[nPosicion]:
            return True
    return False

def fIniciarSesion():
    nIntentos = 3
    while nIntentos > 0:
        print("\n==============================")
        print("       INICIO DE SESIÓN       ")
        print("==============================")
        sUsuario = input("Usuario: ")
        sContrasena = input("Contraseña: ")
        if fVerificarCredenciales(sUsuario, sContrasena):
            print("\nAcceso autorizado.")
            return sUsuario
        nIntentos -= 1
        print("Credenciales incorrectas.")
        if nIntentos > 0:
            print("Intentos restantes:", nIntentos)
    print("\nNúmero máximo de intentos alcanzado.")
    print("Programa finalizado.")
    return False
# Ejecución del programa
if __name__ == "__main__":
    fIniciarSesion()
