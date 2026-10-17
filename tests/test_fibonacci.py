import time

import pytest
from src.fibonacci import (
    fibonacci_iterativo, fibonacci_recursivo, fibonacci_serie,
    es_fibonacci, es_cuadrado_perfecto,
)


def test_fibonacci_iterativo_casos_base():
    # Arrange
    entradas = [0, 1]
    # Act
    resultados = [fibonacci_iterativo(n) for n in entradas]
    # Assert
    assert resultados == [0, 1]


def test_fibonacci_iterativo_valor_10():
    # Arrange
    n = 10
    # Act
    resultado = fibonacci_iterativo(n)
    # Assert
    assert resultado == 55


def test_fibonacci_iterativo_negativo_lanza_error():
    # Arrange
    n = -1
    # Act / Assert
    with pytest.raises(ValueError):
        fibonacci_iterativo(n)


def test_fibonacci_recursivo_casos_base():
    # Arrange
    entradas = [0, 1]
    # Act
    resultados = [fibonacci_recursivo(n) for n in entradas]
    # Assert
    assert resultados == [0, 1]


def test_fibonacci_recursivo_valor_10():
    # Arrange
    n = 10
    # Act
    resultado = fibonacci_recursivo(n)
    # Assert
    assert resultado == 55


def test_fibonacci_recursivo_negativo_lanza_error():
    # Arrange
    n = -1
    # Act / Assert
    with pytest.raises(ValueError):
        fibonacci_recursivo(n)


def test_fibonacci_recursivo_n_grande_es_rapido():
    # Arrange
    n = 36
    # Act
    inicio = time.perf_counter()
    resultado = fibonacci_recursivo(n)
    duracion = time.perf_counter() - inicio
    # Assert
    assert resultado == 14930352
    assert duracion < 0.5


def test_fibonacci_serie_cero():
    # Arrange
    n = 0
    # Act
    resultado = fibonacci_serie(n)
    # Assert
    assert resultado == [0]


def test_fibonacci_serie_uno():
    # Arrange
    n = 1
    # Act
    resultado = fibonacci_serie(n)
    # Assert
    assert resultado == [0, 1]


def test_fibonacci_serie_siete_terminos():
    # Arrange
    n = 7
    # Act
    resultado = fibonacci_serie(n)
    # Assert
    assert resultado == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fibonacci_serie_negativo_lanza_error():
    # Arrange
    n = -3
    # Act / Assert
    with pytest.raises(ValueError):
        fibonacci_serie(n)


def test_es_fibonacci_numero_de_la_serie():
    # Arrange
    numero = 21
    # Act
    resultado = es_fibonacci(numero)
    # Assert
    assert resultado is True


def test_es_fibonacci_numero_que_no_es_de_la_serie():
    # Arrange
    numero = 22
    # Act
    resultado = es_fibonacci(numero)
    # Assert
    assert resultado is False


def test_es_fibonacci_cero_y_uno():
    # Arrange
    numeros = [0, 1]
    # Act
    resultados = [es_fibonacci(n) for n in numeros]
    # Assert
    assert resultados == [True, True]


def test_es_fibonacci_negativo():
    # Arrange
    numero = -5
    # Act
    resultado = es_fibonacci(numero)
    # Assert
    assert resultado is False


def test_es_cuadrado_perfecto_verdadero():
    # Arrange
    numero = 49
    # Act
    resultado = es_cuadrado_perfecto(numero)
    # Assert
    assert resultado is True


def test_es_cuadrado_perfecto_falso():
    # Arrange
    numero = 50
    # Act
    resultado = es_cuadrado_perfecto(numero)
    # Assert
    assert resultado is False


def test_es_cuadrado_perfecto_negativo():
    # Arrange
    numero = -4
    # Act
    resultado = es_cuadrado_perfecto(numero)
    # Assert
    assert resultado is False