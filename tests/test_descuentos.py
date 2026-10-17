import pytest
from src.descuentos import (
    aplicar_descuento, calcular_descuento, calcular_precio_final,
    descuento_por_volumen, descuento_cumulativo, descuento_apilado,
)


def test_aplicar_descuento_valido():
    # Arrange
    precio, porcentaje = 200, 25
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 150


def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -10, 20
    # Act / Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_porcentaje_mayor_a_100_lanza_error():
    # Arrange
    precio, porcentaje = 100, 101
    # Act / Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_calcular_descuento_valido():
    # Arrange
    precio, porcentaje = 200, 10
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 20


def test_calcular_descuento_porcentaje_negativo_lanza_error():
    # Arrange
    precio, porcentaje = 100, -5
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


def test_calcular_precio_final_aplica_impuesto_sobre_precio_con_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 10, 50
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(55)


def test_calcular_precio_final_sin_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 19, 0
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(119)


def test_calcular_precio_final_impuesto_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, -1, 10
    # Act / Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


def test_descuento_por_volumen_sin_descuento():
    # Arrange
    cantidad, precio_unitario = 5, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 50


def test_descuento_por_volumen_10_unidades_5_por_ciento():
    # Arrange
    cantidad, precio_unitario = 10, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(95)


def test_descuento_por_volumen_100_unidades_20_por_ciento():
    # Arrange
    cantidad, precio_unitario = 100, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(800)


def test_descuento_por_volumen_cantidad_negativa_lanza_error():
    # Arrange
    cantidad, precio_unitario = -1, 10
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)


def test_descuento_cumulativo_dos_descuentos():
    # Arrange
    precio, descuentos = 100, [10, 10]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(81)


def test_descuento_cumulativo_lista_vacia_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100


def test_descuento_cumulativo_descuento_invalido_lanza_error():
    # Arrange
    precio, descuentos = 100, [10, 150]
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)


def test_descuento_apilado_suma_porcentajes():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(70)


def test_descuento_apilado_lista_vacia_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100


def test_descuento_apilado_suma_mayor_a_100_no_supera_descuento_total():
    # Arrange
    precio, descuentos = 100, [60, 60]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0


def test_descuento_apilado_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -100, [10]
    # Act / Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)