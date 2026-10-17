import pytest
from src.autenticacion import (
    hash_contraseña, verificar_contraseña, validar_usuario, generar_token,
    validar_token, generar_codigo_2fa, verificar_codigo_2fa, sanear_entrada,
)


def test_hash_contraseña_es_sha256_de_64_caracteres():
    # Arrange
    contraseña = "Secreta123"
    # Act
    resultado = hash_contraseña(contraseña)
    # Assert
    assert len(resultado) == 64


def test_hash_contraseña_misma_entrada_mismo_hash():
    # Arrange
    contraseña = "Secreta123"
    # Act
    hash1 = hash_contraseña(contraseña)
    hash2 = hash_contraseña(contraseña)
    # Assert
    assert hash1 == hash2


def test_hash_contraseña_vacia_lanza_error():
    # Arrange
    contraseña = ""
    # Act / Assert
    with pytest.raises(ValueError):
        hash_contraseña(contraseña)


def test_hash_contraseña_none_lanza_error():
    # Arrange
    contraseña = None
    # Act / Assert
    with pytest.raises(ValueError):
        hash_contraseña(contraseña)


def test_verificar_contraseña_correcta():
    # Arrange
    contraseña = "Secreta123"
    hash_guardado = hash_contraseña(contraseña)
    # Act
    resultado = verificar_contraseña(contraseña, hash_guardado)
    # Assert
    assert resultado is True


def test_verificar_contraseña_incorrecta():
    # Arrange
    hash_guardado = hash_contraseña("Secreta123")
    # Act
    resultado = verificar_contraseña("Otra456", hash_guardado)
    # Assert
    assert resultado is False


def test_validar_usuario_valido():
    # Arrange
    usuario = "juan_12"
    # Act
    resultado = validar_usuario(usuario)
    # Assert
    assert resultado is True


def test_validar_usuario_limites_3_y_20_caracteres():
    # Arrange
    usuarios = ["abc", "a" * 20]
    # Act
    resultados = [validar_usuario(u) for u in usuarios]
    # Assert
    assert resultados == [True, True]


def test_validar_usuario_muy_corto():
    # Arrange
    usuario = "ab"
    # Act
    resultado = validar_usuario(usuario)
    # Assert
    assert resultado is False


def test_validar_usuario_muy_largo():
    # Arrange
    usuario = "a" * 21
    # Act
    resultado = validar_usuario(usuario)
    # Assert
    assert resultado is False


def test_validar_usuario_con_caracteres_invalidos():
    # Arrange
    usuario = "juan perez"
    # Act
    resultado = validar_usuario(usuario)
    # Assert
    assert resultado is False


def test_validar_usuario_vacio():
    # Arrange
    usuario = ""
    # Act
    resultado = validar_usuario(usuario)
    # Assert
    assert resultado is False


def test_generar_token_tiene_formato_valido():
    # Arrange
    usuario, timestamp = "juan", 1700000000
    # Act
    token = generar_token(usuario, timestamp)
    # Assert
    assert validar_token(token) is True


def test_generar_token_no_es_predecible():
    # Arrange
    usuario, timestamp = "juan", 1700000000
    # Act
    token1 = generar_token(usuario, timestamp)
    token2 = generar_token(usuario, timestamp)
    # Assert
    assert token1 != token2


def test_validar_token_valido():
    # Arrange
    token = "a" * 32
    # Act
    resultado = validar_token(token)
    # Assert
    assert resultado is True


def test_validar_token_longitud_incorrecta():
    # Arrange
    token = "a" * 31
    # Act
    resultado = validar_token(token)
    # Assert
    assert resultado is False


def test_validar_token_no_hexadecimal():
    # Arrange
    token = "g" * 32
    # Act
    resultado = validar_token(token)
    # Assert
    assert resultado is False


def test_validar_token_vacio():
    # Arrange
    token = ""
    # Act
    resultado = validar_token(token)
    # Assert
    assert resultado is False


def test_generar_codigo_2fa_tiene_6_digitos():
    # Arrange / Act
    codigo = generar_codigo_2fa()
    # Assert
    assert len(codigo) == 6
    assert codigo.isdigit()


def test_verificar_codigo_2fa_coincide():
    # Arrange
    codigo = "123456"
    # Act
    resultado = verificar_codigo_2fa(codigo, "123456")
    # Assert
    assert resultado is True


def test_verificar_codigo_2fa_no_coincide():
    # Arrange
    codigo = "123456"
    # Act
    resultado = verificar_codigo_2fa(codigo, "654321")
    # Assert
    assert resultado is False


def test_verificar_codigo_2fa_vacio():
    # Arrange
    codigo = ""
    # Act
    resultado = verificar_codigo_2fa(codigo, "123456")
    # Assert
    assert resultado is False


def test_sanear_entrada_elimina_caracteres_peligrosos():
    # Arrange
    entrada = "  <hola>; 'mundo' --  "
    # Act
    resultado = sanear_entrada(entrada)
    # Assert
    assert resultado == "hola mundo"


def test_sanear_entrada_vacia():
    # Arrange
    entrada = ""
    # Act
    resultado = sanear_entrada(entrada)
    # Assert
    assert resultado == ""