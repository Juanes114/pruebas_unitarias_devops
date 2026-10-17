import pytest
from src.manipulador_texto import (
    invertir_cadena, contar_vocales, contar_consonantes, es_palindromo,
    eliminar_duplicados, capitalizar_palabras, reemplazar_subcadena,
    dividir_en_palabras, extraer_dominio, enmascarar_email,
    normalizar_espacios, truncar, es_anagrama, convertir_a_titulo
)


def test_invertir_cadena_valida():
    # Arrange
    cadena = "hola"
    # Act
    resultado = invertir_cadena(cadena)
    # Assert
    assert resultado == "aloh"


def test_invertir_cadena_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = invertir_cadena(cadena)
    # Assert
    assert resultado == ""


def test_contar_vocales_mayusculas_y_minusculas():
    # Arrange
    cadena = "Murcielago AEIOU"
    # Act
    resultado = contar_vocales(cadena)
    # Assert
    assert resultado == 10


def test_contar_consonantes_ignora_vocales_y_simbolos():
    # Arrange
    cadena = "Hola, mundo 123"
    # Act
    resultado = contar_consonantes(cadena)
    # Assert
    assert resultado == 5


def test_es_palindromo_palabra_simple():
    # Arrange
    cadena = "radar"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_es_palindromo_ignora_espacios_y_mayusculas():
    # Arrange
    cadena = "Anita lava la tina"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_es_palindromo_palabra_no_palindromo():
    # Arrange
    cadena = "python"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is False


def test_eliminar_duplicados_conserva_orden():
    # Arrange
    cadena = "banana"
    # Act
    resultado = eliminar_duplicados(cadena)
    # Assert
    assert resultado == "ban"


def test_capitalizar_palabras_varias_palabras():
    # Arrange
    cadena = "hola mundo cruel"
    # Act
    resultado = capitalizar_palabras(cadena)
    # Assert
    assert resultado == "Hola Mundo Cruel"


def test_reemplazar_subcadena_todas_las_apariciones():
    # Arrange
    cadena = "a-b-c"
    # Act
    resultado = reemplazar_subcadena(cadena, "-", "+")
    # Assert
    assert resultado == "a+b+c"


def test_reemplazar_subcadena_con_limite():
    # Arrange
    cadena = "a-b-c"
    # Act
    resultado = reemplazar_subcadena(cadena, "-", "+", 1)
    # Assert
    assert resultado == "a+b-c"


def test_dividir_en_palabras_espacio_simple():
    # Arrange
    cadena = "hola mundo"
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == ["hola", "mundo"]


def test_dividir_en_palabras_multiples_espacios():
    # Arrange
    cadena = "hola   mundo"
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == ["hola", "mundo"]


def test_extraer_dominio_email_valido():
    # Arrange
    email = "ana@unal.edu.co"
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == "unal.edu.co"


def test_extraer_dominio_sin_arroba():
    # Arrange
    email = "ana.unal.edu.co"
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == ""


def test_enmascarar_email_usuario_largo():
    # Arrange
    email = "juanes@gmail.com"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == "j****s@gmail.com"


def test_enmascarar_email_usuario_corto_no_se_modifica():
    # Arrange
    email = "ab@gmail.com"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == "ab@gmail.com"


def test_normalizar_espacios_extra():
    # Arrange
    cadena = "  hola    mundo  "
    # Act
    resultado = normalizar_espacios(cadena)
    # Assert
    assert resultado == "hola mundo"


def test_truncar_cadena_larga_agrega_sufijo():
    # Arrange
    cadena = "Hola mundo cruel"
    # Act
    resultado = truncar(cadena, 10)
    # Assert
    assert resultado == "Hola mu..."


def test_truncar_cadena_corta_no_cambia():
    # Arrange
    cadena = "Hola"
    # Act
    resultado = truncar(cadena, 10)
    # Assert
    assert resultado == "Hola"


def test_es_anagrama_ignora_mayusculas_y_espacios():
    # Arrange
    cadena1, cadena2 = "Roma", "amor"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is True


def test_es_anagrama_cadenas_distintas():
    # Arrange
    cadena1, cadena2 = "hola", "mundo"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is False
    
def test_convertir_a_titulo_valido():
    # Arrange
    cadena = "hola mundo"
    # Act
    resultado = convertir_a_titulo(cadena)
    # Assert
    assert resultado == "Hola Mundo"


def test_convertir_a_titulo_vacio():
    # Arrange
    cadena = ""
    # Act
    resultado = convertir_a_titulo(cadena)
    # Assert
    assert resultado == ""


@pytest.mark.parametrize("funcion, esperado", [
    (contar_vocales, 0),
    (contar_consonantes, 0),
    (es_palindromo, False),
    (eliminar_duplicados, ""),
    (capitalizar_palabras, ""),
    (dividir_en_palabras, []),
    (extraer_dominio, ""),
    (enmascarar_email, ""),
    (normalizar_espacios, ""),
])
def test_funciones_con_cadena_vacia_devuelven_valor_neutro(funcion, esperado):
    # Arrange
    cadena = ""
    # Act
    resultado = funcion(cadena)
    # Assert
    assert resultado == esperado


def test_enmascarar_email_con_dos_arrobas():
    # Arrange
    email = "a@b@c.com"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == ""


def test_extraer_dominio_con_dos_arrobas():
    # Arrange
    email = "a@b@c.com"
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == ""


def test_reemplazar_subcadena_cadena_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = reemplazar_subcadena(cadena, "a", "b")
    # Assert
    assert resultado == ""


def test_truncar_cadena_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = truncar(cadena, 5)
    # Assert
    assert resultado == ""


def test_es_anagrama_con_cadena_vacia():
    # Arrange
    cadena1, cadena2 = "", "abc"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is False