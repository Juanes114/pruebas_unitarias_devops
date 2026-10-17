from src.procesador_texto import (
    contar_palabras, contar_vocales, invertir_texto, es_palindromo,
    eliminar_espacios_extra, convertir_mayusculas, convertir_minusculas,
    capitalizar_palabras, reemplazar_palabra, extraer_iniciales,
    limpiar_texto,
)


def test_contar_palabras_texto_simple():
    # Arrange
    texto = "hola mundo cruel"
    # Act
    resultado = contar_palabras(texto)
    # Assert
    assert resultado == 3


def test_contar_palabras_con_espacios_extra():
    # Arrange
    texto = "  hola    mundo  "
    # Act
    resultado = contar_palabras(texto)
    # Assert
    assert resultado == 2


def test_contar_palabras_texto_vacio():
    # Arrange
    texto = ""
    # Act
    resultado = contar_palabras(texto)
    # Assert
    assert resultado == 0


def test_contar_vocales_mayusculas_y_minusculas():
    # Arrange
    texto = "Murcielago AEIOU"
    # Act
    resultado = contar_vocales(texto)
    # Assert
    assert resultado == 10


def test_invertir_texto_valido():
    # Arrange
    texto = "python"
    # Act
    resultado = invertir_texto(texto)
    # Assert
    assert resultado == "nohtyp"


def test_es_palindromo_palabra_simple():
    # Arrange
    texto = "radar"
    # Act
    resultado = es_palindromo(texto)
    # Assert
    assert resultado is True


def test_es_palindromo_ignora_espacios_y_mayusculas():
    # Arrange
    texto = "Anita lava la tina"
    # Act
    resultado = es_palindromo(texto)
    # Assert
    assert resultado is True


def test_es_palindromo_texto_no_palindromo():
    # Arrange
    texto = "python"
    # Act
    resultado = es_palindromo(texto)
    # Assert
    assert resultado is False


def test_es_palindromo_texto_vacio():
    # Arrange
    texto = ""
    # Act
    resultado = es_palindromo(texto)
    # Assert
    assert resultado is False


def test_eliminar_espacios_extra_texto_con_espacios():
    # Arrange
    texto = "  hola    mundo  "
    # Act
    resultado = eliminar_espacios_extra(texto)
    # Assert
    assert resultado == "hola mundo"


def test_convertir_mayusculas_valido():
    # Arrange
    texto = "hola"
    # Act
    resultado = convertir_mayusculas(texto)
    # Assert
    assert resultado == "HOLA"


def test_convertir_minusculas_valido():
    # Arrange
    texto = "HOLA"
    # Act
    resultado = convertir_minusculas(texto)
    # Assert
    assert resultado == "hola"


def test_capitalizar_palabras_varias_palabras():
    # Arrange
    texto = "hola mundo cruel"
    # Act
    resultado = capitalizar_palabras(texto)
    # Assert
    assert resultado == "Hola Mundo Cruel"


def test_reemplazar_palabra_todas_las_apariciones():
    # Arrange
    texto = "el gato y el perro"
    # Act
    resultado = reemplazar_palabra(texto, "el", "un")
    # Assert
    assert resultado == "un gato y un perro"


def test_extraer_iniciales_nombre_completo():
    # Arrange
    nombre = "juan esteban marulanda"
    # Act
    resultado = extraer_iniciales(nombre)
    # Assert
    assert resultado == "JEM"


def test_extraer_iniciales_texto_vacio():
    # Arrange
    nombre = ""
    # Act
    resultado = extraer_iniciales(nombre)
    # Assert
    assert resultado == ""


def test_limpiar_texto_elimina_caracteres_especiales():
    # Arrange
    texto = "Hola, mundo! #2024"
    # Act
    resultado = limpiar_texto(texto)
    # Assert
    assert resultado == "Hola mundo 2024"


def test_limpiar_texto_vacio():
    # Arrange
    texto = ""
    # Act
    resultado = limpiar_texto(texto)
    # Assert
    assert resultado == ""