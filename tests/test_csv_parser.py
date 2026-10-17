from src.csv_parser import (
    parse_csv_line, leer_csv_como_lista, csv_a_diccionarios, validar_csv,
    extraer_columna, filtrar_por_columna, contar_filas, contar_columnas,
)

CSV_BASICO = "nombre,edad\nAna,20\nLuis,30"


def test_parse_csv_line_simple():
    # Arrange
    linea = "a,b,c"
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["a", "b", "c"]


def test_parse_csv_line_vacia():
    # Arrange
    linea = ""
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == []


def test_parse_csv_line_coma_dentro_de_comillas():
    # Arrange
    linea = 'a,"b,c",d'
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["a", "b,c", "d"]


def test_parse_csv_line_comillas_escapadas():
    # Arrange
    linea = 'a,"dijo ""hola""",c'
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["a", 'dijo "hola"', "c"]


def test_leer_csv_como_lista_varias_filas():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == [["nombre", "edad"], ["Ana", "20"], ["Luis", "30"]]


def test_leer_csv_como_lista_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == []


def test_csv_a_diccionarios_con_cabecera():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == [
        {"nombre": "Ana", "edad": "20"},
        {"nombre": "Luis", "edad": "30"},
    ]


def test_csv_a_diccionarios_fila_con_menos_columnas():
    # Arrange
    contenido = "nombre,edad\nAna"
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == [{"nombre": "Ana", "edad": ""}]


def test_csv_a_diccionarios_solo_cabecera():
    # Arrange
    contenido = "nombre,edad"
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == []


def test_csv_a_diccionarios_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == []


def test_validar_csv_formato_consistente():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is True


def test_validar_csv_filas_con_distinto_numero_de_columnas():
    # Arrange
    contenido = "a,b\n1,2,3"
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False


def test_validar_csv_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False


def test_extraer_columna_existente():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = extraer_columna(contenido, 0)
    # Assert
    assert resultado == ["nombre", "Ana", "Luis"]


def test_extraer_columna_indice_fuera_de_rango():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = extraer_columna(contenido, 5)
    # Assert
    assert resultado == ["", "", ""]


def test_extraer_columna_csv_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = extraer_columna(contenido, 0)
    # Assert
    assert resultado == []


def test_filtrar_por_columna_con_coincidencia():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = filtrar_por_columna(contenido, 0, "Ana")
    # Assert
    assert resultado == [["Ana", "20"]]


def test_filtrar_por_columna_sin_coincidencia():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = filtrar_por_columna(contenido, 0, "Pedro")
    # Assert
    assert resultado == []


def test_filtrar_por_columna_csv_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = filtrar_por_columna(contenido, 0, "Ana")
    # Assert
    assert resultado == []


def test_contar_filas_con_datos():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 3


def test_contar_filas_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 0


def test_contar_columnas_con_datos():
    # Arrange
    contenido = CSV_BASICO
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 2


def test_contar_columnas_con_coma_entre_comillas():
    # Arrange
    contenido = 'a,"b,c",d'
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 3


def test_contar_columnas_vacio():
    # Arrange
    contenido = ""
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 0