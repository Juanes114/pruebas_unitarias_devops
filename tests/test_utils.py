import pytest
from src.utils import (
    celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin,
    kelvin_a_celsius, calcular_imc, categorizar_imc, calcular_edad,
    es_bisiesto, dias_en_mes, es_primo, mcd, mcm,
)


def test_celsius_a_fahrenheit_punto_de_ebullicion():
    # Arrange
    celsius = 100
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 212


def test_fahrenheit_a_celsius_punto_de_congelacion():
    # Arrange
    fahrenheit = 32
    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)
    # Assert
    assert resultado == 0


def test_celsius_a_kelvin_cero_celsius():
    # Arrange
    celsius = 0
    # Act
    resultado = celsius_a_kelvin(celsius)
    # Assert
    assert resultado == pytest.approx(273.15)


def test_kelvin_a_celsius_273_kelvin():
    # Arrange
    kelvin = 273.15
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(0)


def test_calcular_imc_valido():
    # Arrange
    peso, altura = 70, 1.75
    # Act
    resultado = calcular_imc(peso, altura)
    # Assert
    assert resultado == pytest.approx(22.857, rel=1e-3)


def test_calcular_imc_peso_invalido_lanza_error():
    # Arrange
    peso, altura = 0, 1.75
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_imc(peso, altura)


def test_calcular_imc_altura_invalida_lanza_error():
    # Arrange
    peso, altura = 70, 0
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_imc(peso, altura)


def test_categorizar_imc_en_cada_rango():
    # Arrange
    valores = [17, 22, 27, 35]
    # Act
    resultados = [categorizar_imc(v) for v in valores]
    # Assert
    assert resultados == ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]


def test_categorizar_imc_en_los_limites():
    # Arrange
    valores = [18.5, 25, 30]
    # Act
    resultados = [categorizar_imc(v) for v in valores]
    # Assert
    assert resultados == ["Normal", "Sobrepeso", "Obesidad"]


def test_calcular_edad_valida():
    # Arrange
    nacimiento, actual = 2000, 2024
    # Act
    resultado = calcular_edad(nacimiento, actual)
    # Assert
    assert resultado == 24


def test_calcular_edad_nacimiento_futuro_lanza_error():
    # Arrange
    nacimiento, actual = 2030, 2024
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_edad(nacimiento, actual)


def test_es_bisiesto_casos_comunes():
    # Arrange
    anios = [2024, 2023, 1900, 2000]
    # Act
    resultados = [es_bisiesto(a) for a in anios]
    # Assert
    assert resultados == [True, False, False, True]


def test_dias_en_mes_de_30_y_31_dias():
    # Arrange
    meses = [4, 1]
    # Act
    resultados = [dias_en_mes(m, 2024) for m in meses]
    # Assert
    assert resultados == [30, 31]


def test_dias_en_mes_febrero_bisiesto_y_no_bisiesto():
    # Arrange
    anios = [2024, 2023]
    # Act
    resultados = [dias_en_mes(2, a) for a in anios]
    # Assert
    assert resultados == [29, 28]


def test_dias_en_mes_invalido_lanza_error():
    # Arrange
    mes = 13
    # Act / Assert
    with pytest.raises(ValueError):
        dias_en_mes(mes, 2024)


def test_es_primo_numeros_primos():
    # Arrange
    numeros = [2, 3, 17, 97]
    # Act
    resultados = [es_primo(n) for n in numeros]
    # Assert
    assert resultados == [True, True, True, True]


def test_es_primo_numeros_no_primos():
    # Arrange
    numeros = [-3, 0, 1, 9, 100]
    # Act
    resultados = [es_primo(n) for n in numeros]
    # Assert
    assert resultados == [False, False, False, False, False]


def test_mcd_valido():
    # Arrange
    a, b = 12, 18
    # Act
    resultado = mcd(a, b)
    # Assert
    assert resultado == 6


def test_mcm_valido():
    # Arrange
    a, b = 4, 6
    # Act
    resultado = mcm(a, b)
    # Assert
    assert resultado == 12


def test_mcm_con_cero_devuelve_cero():
    # Arrange
    a, b = 0, 5
    # Act
    resultado = mcm(a, b)
    # Assert
    assert resultado == 0


def test_mcm_de_ceros_no_lanza_error():
    # Arrange
    a, b = 0, 0
    # Act
    resultado = mcm(a, b)
    # Assert
    assert resultado == 0


def test_mcm_con_negativos_es_positivo():
    # Arrange
    a, b = -4, 6
    # Act
    resultado = mcm(a, b)
    # Assert
    assert resultado == 12