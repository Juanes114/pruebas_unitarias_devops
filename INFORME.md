# Informe: Taller de pruebas unitarias (DevOps)

## 1. Datos

- **Estudiante:** Juan Esteban Marulanda Zapata
- **Curso:** Introducción a DevOps
- **Docente:** Cesar Augusto Palacios
- **Fecha de entrega:** 17/10/2026
- **Repositorio (fork):** https://github.com/Juanes114/pruebas_unitarias_devops
- **Herramientas:** Python 3.12.2, pytest 8.0.0, pytest-cov 4.0.0

**Resultado general:** 244 pruebas (estructura AAA) en 10 módulos, **16 bugs** encontrados y corregidos (el taller pedía 3) y **96 % de cobertura total**, con todos los módulos por encima del 85 %. Cada módulo se trabajó en dos commits: uno con las pruebas (`test:`) y otro con la corrección (`fix:`), de modo que el historial muestra primero el fallo y luego el arreglo.

## 2. Análisis por módulo

Criterio general: por cada función probé (a) un caso normal, (b) los límites o valores frontera y (c) las entradas inválidas, esperando una excepción cuando el código la declara. Los bugs aparecieron casi siempre en el grupo (b) o (c), no en el caso normal.

| Módulo | Pruebas | Qué probé y por qué | Bugs |
|---|---|---|---|
| `calculadora` | 19 | Operaciones básicas con un caso normal, división por cero, lista vacía y negativos. `minimo` se probó con una lista de positivos, porque un valor inicial fijo en 0 solo falla ahí. | 2 |
| `conversor` | 31 | Un valor conocido por conversión (100 °C = 212 °F, 32 °F = 0 °C) y entradas negativas, que deben lanzar error. Se comparó con `pytest.approx` para evitar errores de coma flotante. | 2 |
| `descuentos` | 19 | Descuento y precio final con valores calculables a mano, porcentajes fuera de 0–100 y los tramos de descuento por volumen (5, 10 y 100 unidades). | 2 |
| `manipulador_texto` | 38 | Texto vacío, mayúsculas/minúsculas, espacios múltiples y emails con usuario corto o sin arroba. Un palíndromo con espacios y mayúsculas revela el bug de limpieza. | 2 |
| `validador` | 31 | Casos válidos, inválidos y límites de cada validador. En fechas probé días 31 en meses de 30, febrero bisiesto y no bisiesto, porque ahí falla la lógica. | 1 |
| `procesador_texto` | 18 | Conteo, inversión y limpieza de texto, con vacío y espacios extra. Mismo caso de palíndromo que en `manipulador_texto`. | 1 |
| `fibonacci` | 18 | Casos base (0 y 1), un valor conocido, negativos y la serie. Añadí una prueba de **tiempo** con `n = 36` porque el defecto es de rendimiento, no de resultado. | 1 |
| `autenticacion` | 24 | Hash determinista, contraseña vacía y `None`, límites de 3 y 20 caracteres en usuario, formato del token y 2FA. Dos tokens con la misma entrada deben diferir. | 2 |
| `csv_parser` | 24 | Líneas simples, comas dentro de comillas, comillas escapadas y filas con menos columnas que la cabecera. | 2 |
| `utils` | 22 | Conversiones, IMC en cada rango y en los límites 18.5, 25 y 30, años bisiestos, primos y `mcm` con cero y negativos. | 1 |

## 3. Tabla de bugs

| # | Módulo / función | Entrada que lo revela | Obtenido | Esperado | Corrección |
|---|---|---|---|---|---|
| 1 | `calculadora.raiz_cuadrada` | `-4` | Sin error (devolvía un número complejo) | `ValueError` | Validar `numero < 0` |
| 2 | `calculadora.minimo` | `[3, 5, 9]` | `0` | `3` | Inicializar con `lista[0]` |
| 3 | `conversor.kelvin_a_celsius` | `-5` | Sin error (`-278.15`) | `ValueError` | Validar `kelvin < 0` |
| 4 | `conversor.kilometros_a_millas` | `16.0934` | `25.8997…` | `10` | Dividir en vez de multiplicar |
| 5 | `descuentos.calcular_precio_final` | `(100, 10, 50)` | `60.0` | `55` | Calcular el impuesto sobre el precio ya descontado |
| 6 | `descuentos.descuento_apilado` | `(100, [60, 60])` | `ValueError` | `0` (tope del 100 %) | `min(sum(descuentos), 100)` |
| 7 | `manipulador_texto.es_palindromo` | `"Anita lava la tina"` | `False` | `True` | Quitar no alfanuméricos y pasar a minúsculas |
| 8 | `manipulador_texto.dividir_en_palabras` | `"hola   mundo"` | `['hola', '', '', 'mundo']` | `['hola', 'mundo']` | Usar `split()` sin argumento |
| 9 | `validador.validar_fecha` | `(31, 2, 2024)`, `(31, 4, 2024)`, `(29, 2, 2023)` | `True` | `False` | `calendar.monthrange` para los días reales del mes |
| 10 | `procesador_texto.es_palindromo` | `"Anita lava la tina"` | `False` | `True` | Misma limpieza que en el #7 |
| 11 | `fibonacci.fibonacci_recursivo` | `n = 36` | 8.56 s | < 0.5 s | Memoización con `functools.lru_cache` |
| 12 | `autenticacion.hash_contraseña` | `None` y `""` | `AttributeError` / sin error | `ValueError` | Validar que la contraseña no esté vacía |
| 13 | `autenticacion.generar_token` | Misma entrada dos veces | Tokens idénticos | Tokens distintos | Agregar sal aleatoria con `secrets.token_hex` |
| 14 | `csv_parser.parse_csv_line` | `a,"b,c",d` | `['a', '"b', 'c"', 'd']` | `['a', 'b,c', 'd']` | Usar `csv.reader` |
| 15 | `csv_parser.csv_a_diccionarios` | `"nombre,edad\nAna"` | `[{'nombre': 'Ana'}]` | `[{'nombre': 'Ana', 'edad': ''}]` | Recorrer las cabeceras y rellenar con `""` |
| 16 | `utils.mcm` | `(0, 0)` y `(-4, 6)` | `ZeroDivisionError` / `-12` | `0` / `12` | Devolver 0 si algún valor es 0 y usar valores absolutos |

**Notas de criterio:**
- El #6 es una decisión de diseño: el código original lanzaba error cuando la suma de descuentos superaba 100 %. Lo traté como defecto porque el propio repositorio lo marca como bug ("el descuento total puede exceder el 100 %"), y lo resolví limitando el descuento al 100 %.
- El #11 es un defecto de rendimiento: el resultado era correcto, pero la versión recursiva recalculaba los mismos valores una y otra vez.
- El #13 queda con una limitación conocida: el token sigue usando MD5, que es débil, pero cambiarlo rompería `validar_token`, que espera 32 caracteres hexadecimales.

## 4. Ejecuciones clave

### 4.1 Pruebas en rojo (bugs detectados antes de corregir)

Resumen de los fallos de cada módulo, tal como los mostró pytest antes de la corrección (los conteos de pruebas son los de ese momento, previos a las pruebas adicionales de cobertura):

```text
FAILED tests/test_calculadora.py::test_raiz_cuadrada_negativo_lanza_error - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_calculadora.py::test_minimo_lista_de_positivos - assert 0 == 3
→ 2 failed, 10 passed in 0.30s

FAILED tests/test_conversor.py::test_kelvin_a_celsius_negativo_lanza_error - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_conversor.py::test_kilometros_a_millas_valido - assert 25.899752355999997 == 10 ± 1.0e-05
→ 2 failed, 17 passed in 0.37s

FAILED tests/test_descuentos.py::test_calcular_precio_final_aplica_impuesto_sobre_precio_con_descuento - assert 60.0 == 55 ± 5.5e-05
FAILED tests/test_descuentos.py::test_descuento_apilado_suma_mayor_a_100_no_supera_descuento_total - ValueError: El porcentaje debe estar entre 0 y 100
→ 2 failed, 17 passed in 0.36s

FAILED tests/test_manipulador_texto.py::test_es_palindromo_ignora_espacios_y_mayusculas - assert False is True
FAILED tests/test_manipulador_texto.py::test_dividir_en_palabras_multiples_espacios - AssertionError: assert ['hola', '', '', 'mundo'] == ['hola', 'mundo']
→ 2 failed, 20 passed in 0.38s

FAILED tests/test_validador.py::test_validar_fecha_31_de_febrero_es_invalida - assert True is False
FAILED tests/test_validador.py::test_validar_fecha_31_de_abril_es_invalida - assert True is False
FAILED tests/test_validador.py::test_validar_fecha_29_febrero_anio_no_bisiesto - assert True is False
→ 3 failed, 28 passed in 0.45s

FAILED tests/test_procesador_texto.py::test_es_palindromo_ignora_espacios_y_mayusculas - assert False is True
→ 1 failed, 17 passed in 0.36s

FAILED tests/test_fibonacci.py::test_fibonacci_recursivo_n_grande_es_rapido - assert 8.563689200003864 < 0.5
→ 1 failed, 17 passed in 8.89s

FAILED tests/test_autenticacion.py::test_hash_contraseña_vacia_lanza_error - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_autenticacion.py::test_hash_contraseña_none_lanza_error - AttributeError: 'NoneType' object has no attribute 'encode'
FAILED tests/test_autenticacion.py::test_generar_token_no_es_predecible - AssertionError: assert '7ce2e6453792757062ac19496250f50e' != '7ce2e6453792757062ac19496250f50e'
→ 3 failed, 21 passed in 0.46s

FAILED tests/test_csv_parser.py::test_parse_csv_line_coma_dentro_de_comillas - assert ['a', '"b', 'c"', 'd'] == ['a', 'b,c', 'd']
FAILED tests/test_csv_parser.py::test_parse_csv_line_comillas_escapadas - assert ['a', '"dijo ""hola"""', 'c'] == ['a', 'dijo "hola"', 'c']
FAILED tests/test_csv_parser.py::test_csv_a_diccionarios_fila_con_menos_columnas - AssertionError: assert [{'nombre': 'Ana'}] == [{'nombre': '..., 'edad': ''}]
FAILED tests/test_csv_parser.py::test_contar_columnas_con_coma_entre_comillas - assert 4 == 3
→ 4 failed, 20 passed in 0.83s

FAILED tests/test_utils.py::test_mcm_de_ceros_no_lanza_error - ZeroDivisionError: integer division or modulo by zero
FAILED tests/test_utils.py::test_mcm_con_negativos_es_positivo - assert -12 == 12
→ 2 failed, 20 passed in 0.45s
```

Dos tracebacks completos como ejemplo:

```text
    def test_fibonacci_recursivo_n_grande_es_rapido():
        # Arrange
        n = 36
        # Act
        inicio = time.perf_counter()
        resultado = fibonacci_recursivo(n)
        duracion = time.perf_counter() - inicio
        # Assert
        assert resultado == 14930352
>       assert duracion < 0.5
E       assert 8.563689200003864 < 0.5

tests\test_fibonacci.py:71: AssertionError
```

```text
contraseña = None

    def hash_contraseña(contraseña):
        """Genera un hash SHA-256 de una contraseña."""
        # BUG 1: No maneja contraseñas vacías o None
>       return hashlib.sha256(contraseña.encode()).hexdigest()
E       AttributeError: 'NoneType' object has no attribute 'encode'

src\autenticacion.py:12: AttributeError
```

### 4.2 Pruebas en verde y cobertura (después de corregir)

Comando: `pytest --cov=src --cov-report=term-missing`

```text
---------- coverage: platform win32, python 3.12.2-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src\__init__.py                0      0   100%
src\autenticacion.py          46      0   100%
src\calculadora.py            44      0   100%
src\conversor.py              58      4    93%   46, 58, 83, 95
src\csv_parser.py             73      2    97%   60, 118
src\descuentos.py             58      7    88%   20, 30, 36, 54, 62, 64, 75
src\fibonacci.py              44      0   100%
src\manipulador_texto.py      93      0   100%
src\procesador_texto.py       50      7    86%   17, 25, 40, 47, 53, 59, 65
src\utils.py                  55      0   100%
src\validador.py              65      5    92%   14, 33, 61, 83, 109
--------------------------------------------------------
TOTAL                        586     25    96%

244 passed in 2.68s
```

## 5. Análisis de cobertura

La cobertura total es del **96 %** (561 de 586 líneas), por encima de la meta del 85 %, y **ningún módulo queda por debajo de esa meta**. Cinco módulos llegan al 100 % (`autenticacion`, `calculadora`, `fibonacci`, `manipulador_texto` y `utils`); `csv_parser`, `conversor` y `validador` superan el 90 %, y `descuentos` y `procesador_texto` están en 88 % y 86 %.

En una primera medición (91 % total) `calculadora`, `conversor` y `manipulador_texto` estaban entre 82 % y 83 %. Agregué pruebas para las funciones que no había cubierto y para las ramas de entrada vacía o negativa, usando pruebas parametrizadas para no repetir código.

Lo que sigue sin cubrir son, sobre todo, guardas de entrada inválida o vacía en funciones que ya probé con su caso normal, y dos tramos intermedios del descuento por volumen (`descuentos`). Son líneas de bajo riesgo y las dejé fuera a propósito, porque priorizar los casos con bugs aporta más que perseguir el 100 %.

## 6. Reflexión final

Lo más valioso del taller fue ver que **una prueba que falla es la forma más clara de describir un bug**: cada defecto quedó documentado por una entrada concreta, un resultado obtenido y uno esperado, antes de tocar el código. Trabajar en dos commits por módulo (primero la prueba, luego la corrección) hizo ese proceso visible en el historial.

Tuve un error propio que me enseñó algo: al principio pegué la función corregida dentro del archivo de pruebas, y las pruebas pasaban aunque `src/` seguía con el bug. Las pruebas deben **importar el código real**, y solo la ejecución en rojo antes de corregir confirma que la prueba de verdad detecta el defecto.

También aprendí que no todos los bugs son de resultado: `fibonacci_recursivo` devolvía valores correctos pero era inutilizable por lento, y `generar_token` era predecible. Y que una cobertura alta no equivale a calidad: el 96 % mide líneas ejecutadas, no que cada caso límite esté bien razonado. Para un flujo DevOps real, estas pruebas serían el paso previo en la integración continua: ningún cambio entra al repositorio si alguna de las 244 pruebas falla.
