import pytest
from src.calculadora import (
    sumar, restar, dividir, raiz_cuadrada, promedio, maximo, minimo,
    calcular_area_rectangulo,
)


def test_sumar_positivos():
    # Arrange
    a, b = 5, 3
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 8


def test_restar_resultado_negativo():
    # Arrange
    a, b = 3, 5
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -2


def test_dividir_numeros_validos():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 2.5


def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act / Assert
    with pytest.raises(ValueError):
        dividir(a, b)


def test_raiz_cuadrada_de_nueve():
    # Arrange
    numero = 9
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 3


def test_raiz_cuadrada_negativo_lanza_error():  # BUG 1
    # Arrange
    numero = -4
    # Act / Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


def test_promedio_lista_simple():
    # Arrange
    lista = [2, 4, 6]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 4


def test_promedio_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act / Assert
    with pytest.raises(ValueError):
        promedio(lista)


def test_maximo_lista_con_negativos():
    # Arrange
    lista = [-5, -1, -9]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == -1


def test_minimo_lista_de_positivos():  # BUG 2
    # Arrange
    lista = [3, 5, 9]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 3


def test_area_rectangulo_valido():
    # Arrange
    base, altura = 4, 5
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 20


def test_area_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = -1, 5
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)