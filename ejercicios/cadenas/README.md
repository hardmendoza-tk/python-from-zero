# Ejercicio 01 — Analizador de texto

> **Tipo:** ejercicio personal de práctica de Python.  
> **Estado:** código original conservado, sin refactorización.  
> **Archivo:** [`analizador_texto.py`](analizador_texto.py).

## Propósito

Este programa de consola recibe una frase escrita por el usuario y muestra distintas transformaciones y propiedades del texto. Es uno de mis ejercicios iniciales mientras aprendía Python.

## Conceptos que practiqué

- **Entrada y salida:** `input()` y `print()`.
- **Variables y cadenas de texto:** almacenar y procesar el contenido introducido.
- **Métodos de cadenas:** `.lower()`, `.upper()`, `.strip()`, `.split()` y `.replace()`.
- **Longitud:** `len()` para contar palabras después de separar el texto.
- **Índices:** `[0]` y `[-1]` para acceder al primer y último carácter.
- **Slicing:** `[::-1]` para invertir la cadena.
- **Pertenencia y negación:** `in` y `not in` para comprobaciones sencillas.
- **Iteración:** `for` para reemplazar vocales una por una.
- **Expresiones formateadas:** cadenas `f"..."` para presentar los resultados.

## Qué hace el programa

1. Solicita un texto y lo convierte a minúsculas.
2. Elimina espacios al principio y al final para crear una versión limpia.
3. Muestra el texto transformado a mayúsculas y minúsculas.
4. Separa el texto en palabras y cuenta cuántas hay.
5. Muestra su primer y último carácter.
6. Realiza comprobaciones básicas sobre vocales y consonantes.
7. Invierte el texto.
8. Reemplaza las vocales `a, e, i, o, u` por asteriscos.

## Ejecución

Desde la raíz del repositorio:

```bash
python ejercicios/cadenas/analizador_texto.py
```

En ciertos sistemas se utiliza `python3` en lugar de `python`. Escribe una frase cuando aparezca la solicitud de texto.

## Notas sobre la versión original

El objetivo de este ejercicio fue practicar operaciones básicas, **no crear una herramienta completa para analizar lenguaje**. Se conserva el código tal como fue escrito originalmente.

Limitaciones observadas al leer el código:

- Una entrada vacía puede causar un `IndexError` al acceder al primer carácter; una entrada de solo espacios también puede causarlo tras aplicar `strip()`.
- La variable llamada `texto` ya contiene una versión en minúsculas: la salida etiquetada como «texto original» no conserva necesariamente las mayúsculas introducidas.
- La comprobación de si el texto comienza por vocal incluye un espacio entre los caracteres aceptados.
- La comprobación de «termina en consonante» utiliza `not in "aeiou"`, por lo que también puede clasificar signos, números o espacios como si fueran consonantes.
- El reemplazo de vocales es una operación sencilla sobre las cinco vocales sin acentos.

Estas observaciones están documentadas para mostrar el aprendizaje y señalar posibles mejoras futuras; **no se ha modificado el código Python**.
