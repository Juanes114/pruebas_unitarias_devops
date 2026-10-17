from src.validador import (
    validar_email, validar_telefono, validar_edad, validar_password,
    validar_url, validar_fecha, validar_cedula,
)


def test_validar_email_valido():
    # Arrange
    email = "ana@unal.edu.co"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is True


def test_validar_email_sin_punto_en_dominio():
    # Arrange
    email = "ana@unal"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False


def test_validar_email_sin_usuario():
    # Arrange
    email = "@unal.edu.co"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False


def test_validar_email_dos_arrobas():
    # Arrange
    email = "ana@@unal.edu.co"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False


def test_validar_email_vacio():
    # Arrange
    email = ""
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False


def test_validar_telefono_con_espacios_y_guiones():
    # Arrange
    telefono = "300 123-4567"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is True


def test_validar_telefono_muy_corto():
    # Arrange
    telefono = "123456"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is False


def test_validar_telefono_con_letras():
    # Arrange
    telefono = "abc1234567"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is False


def test_validar_edad_valida():
    # Arrange
    edad = 25
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is True


def test_validar_edad_negativa():
    # Arrange
    edad = -1
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False


def test_validar_edad_mayor_a_120():
    # Arrange
    edad = 121
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False


def test_validar_edad_no_entero():
    # Arrange
    edad = "25"
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False


def test_validar_password_valida():
    # Arrange
    password = "Abcdefg1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is True


def test_validar_password_corta():
    # Arrange
    password = "Ab1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False


def test_validar_password_sin_mayuscula():
    # Arrange
    password = "abcdefg1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False


def test_validar_password_sin_minuscula():
    # Arrange
    password = "ABCDEFG1"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False


def test_validar_password_sin_numero():
    # Arrange
    password = "Abcdefgh"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False


def test_validar_url_valida():
    # Arrange
    url = "https://google.com"
    # Act
    resultado = validar_url(url)
    # Assert
    assert resultado is True


def test_validar_url_sin_protocolo():
    # Arrange
    url = "google.com"
    # Act
    resultado = validar_url(url)
    # Assert
    assert resultado is False


def test_validar_fecha_valida():
    # Arrange
    dia, mes, anio = 15, 6, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is True


def test_validar_fecha_31_de_febrero_es_invalida():
    # Arrange
    dia, mes, anio = 31, 2, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_fecha_31_de_abril_es_invalida():
    # Arrange
    dia, mes, anio = 31, 4, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_fecha_29_febrero_anio_bisiesto():
    # Arrange
    dia, mes, anio = 29, 2, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is True


def test_validar_fecha_29_febrero_anio_no_bisiesto():
    # Arrange
    dia, mes, anio = 29, 2, 2023
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_fecha_mes_invalido():
    # Arrange
    dia, mes, anio = 1, 13, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_fecha_anio_fuera_de_rango():
    # Arrange
    dia, mes, anio = 1, 1, 1800
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_fecha_valores_no_enteros():
    # Arrange
    dia, mes, anio = "1", 1, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_cedula_valida():
    # Arrange
    cedula = "1234567890"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is True


def test_validar_cedula_con_letras():
    # Arrange
    cedula = "12345abc"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False


def test_validar_cedula_muy_corta():
    # Arrange
    cedula = "12345"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False


def test_validar_cedula_muy_larga():
    # Arrange
    cedula = "12345678901"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False