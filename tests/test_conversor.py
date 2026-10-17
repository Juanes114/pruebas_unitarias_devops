import pytest
from src.conversor import (
    celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin,
    kelvin_a_celsius, metros_a_kilometros, kilometros_a_metros,
    libras_a_kilogramos, kilogramos_a_libras, galones_a_litros,
    litros_a_galones, millas_a_kilometros, kilometros_a_millas,
    pies_a_metros, metros_a_pies, onzas_a_gramos, gramos_a_onzas,
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


def test_kelvin_a_celsius_valido():
    # Arrange
    kelvin = 273.15
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(0)


def test_kelvin_a_celsius_negativo_lanza_error():
    # Arrange
    kelvin = -5
    # Act / Assert
    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)


def test_metros_a_kilometros_valido():
    # Arrange
    metros = 2500
    # Act
    resultado = metros_a_kilometros(metros)
    # Assert
    assert resultado == 2.5


def test_metros_a_kilometros_negativo_lanza_error():
    # Arrange
    metros = -1
    # Act / Assert
    with pytest.raises(ValueError):
        metros_a_kilometros(metros)


def test_kilometros_a_metros_valido():
    # Arrange
    kilometros = 3
    # Act
    resultado = kilometros_a_metros(kilometros)
    # Assert
    assert resultado == 3000


def test_libras_a_kilogramos_valido():
    # Arrange
    libras = 10
    # Act
    resultado = libras_a_kilogramos(libras)
    # Assert
    assert resultado == pytest.approx(4.53592)


def test_kilogramos_a_libras_negativo_lanza_error():
    # Arrange
    kilogramos = -2
    # Act / Assert
    with pytest.raises(ValueError):
        kilogramos_a_libras(kilogramos)


def test_galones_a_litros_valido():
    # Arrange
    galones = 2
    # Act
    resultado = galones_a_litros(galones)
    # Assert
    assert resultado == pytest.approx(7.57082)


def test_litros_a_galones_negativo_lanza_error():
    # Arrange
    litros = -1
    # Act / Assert
    with pytest.raises(ValueError):
        litros_a_galones(litros)


def test_millas_a_kilometros_valido():
    # Arrange
    millas = 10
    # Act
    resultado = millas_a_kilometros(millas)
    # Assert
    assert resultado == pytest.approx(16.0934)


def test_kilometros_a_millas_valido():
    # Arrange
    kilometros = 16.0934
    # Act
    resultado = kilometros_a_millas(kilometros)
    # Assert
    assert resultado == pytest.approx(10)


def test_kilometros_a_millas_negativo_lanza_error():
    # Arrange
    kilometros = -3
    # Act / Assert
    with pytest.raises(ValueError):
        kilometros_a_millas(kilometros)


def test_pies_a_metros_valido():
    # Arrange
    pies = 10
    # Act
    resultado = pies_a_metros(pies)
    # Assert
    assert resultado == pytest.approx(3.048)


def test_metros_a_pies_negativo_lanza_error():
    # Arrange
    metros = -1
    # Act / Assert
    with pytest.raises(ValueError):
        metros_a_pies(metros)


def test_onzas_a_gramos_valido():
    # Arrange
    onzas = 2
    # Act
    resultado = onzas_a_gramos(onzas)
    # Assert
    assert resultado == pytest.approx(56.699)


def test_gramos_a_onzas_negativo_lanza_error():
    # Arrange
    gramos = -10
    # Act / Assert
    with pytest.raises(ValueError):
        gramos_a_onzas(gramos)
        
@pytest.mark.parametrize("funcion", [
    metros_a_kilometros, kilometros_a_metros, libras_a_kilogramos,
    kilogramos_a_libras, galones_a_litros, litros_a_galones,
    millas_a_kilometros, kilometros_a_millas, pies_a_metros,
    metros_a_pies, onzas_a_gramos, gramos_a_onzas,
])
def test_conversiones_con_valor_negativo_lanzan_error(funcion):
    # Arrange
    valor = -1
    # Act / Assert
    with pytest.raises(ValueError):
        funcion(valor)