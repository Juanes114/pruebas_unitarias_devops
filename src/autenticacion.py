"""
Módulo de autenticación y seguridad.
ATENCIÓN: Hay 2 bugs ocultos en este archivo.
"""

import hashlib
import re
import secrets

def hash_contraseña(contraseña):
    """Genera un hash SHA-256 de una contraseña."""
    if not contraseña:
        raise ValueError("La contraseña no puede estar vacía")
    return hashlib.sha256(contraseña.encode()).hexdigest()

def verificar_contraseña(contraseña, hash_guardado):
    """Verifica si una contraseña coincide con el hash."""
    hash_nuevo = hash_contraseña(contraseña)
    return hash_nuevo == hash_guardado

def validar_usuario(usuario):
    """Valida si un nombre de usuario es válido."""
    if not usuario:
        return False

    # Debe tener entre 3 y 20 caracteres
    if len(usuario) < 3 or len(usuario) > 20:
        return False

    # Solo letras, números y guiones bajos
    if not re.match(r'^[a-zA-Z0-9_]+$', usuario):
        return False

    return True

def generar_token(usuario, timestamp):
    """Genera un token simple basado en usuario y timestamp."""
    sal = secrets.token_hex(16)
    datos = f"{usuario}:{timestamp}:{sal}"
    return hashlib.md5(datos.encode()).hexdigest()

def validar_token(token):
    """Valida si un token tiene formato correcto."""
    if not token:
        return False

    # Debe ser un hash MD5 válido (32 caracteres hexadecimales)
    if len(token) != 32:
        return False

    try:
        int(token, 16)
        return True
    except ValueError:
        return False

def generar_codigo_2fa():
    """Genera un código de 2 factores de 6 dígitos."""
    import random
    return str(random.randint(100000, 999999))

def verificar_codigo_2fa(codigo, codigo_guardado):
    """Verifica si un código 2FA coincide."""
    if not codigo or not codigo_guardado:
        return False

    return codigo == codigo_guardado

def sanear_entrada(entrada):
    """Sanea una entrada de usuario para evitar inyección básica."""
    if not entrada:
        return ""

    # Eliminar caracteres peligrosos
    entrada_limpia = entrada.replace("<", "").replace(">", "")
    entrada_limpia = entrada_limpia.replace("'", "").replace('"', "")
    entrada_limpia = entrada_limpia.replace(";", "").replace("--", "")

    return entrada_limpia.strip()