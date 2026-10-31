# Ejercicio 02 — Analizador de contraseñas

> **Tipo:** ejercicio personal de práctica de Python.  
> **Estado:** código original conservado, sin cambios.  
> **Archivo:** [`password_analyzer.py`](password_analyzer.py).

## Descripción

Ejercicio de consola que solicita una contraseña y comprueba algunas características de sus caracteres. Fue desarrollado como práctica de fundamentos de Python, expresiones booleanas y estructuras condicionales. **No es una herramienta de seguridad real ni un validador listo para producción.**

## Conceptos practicados

- **Entrada y salida:** `input()` y `print()`.
- **Cadenas:** `len()` para comprobar una longitud mínima de ocho caracteres.
- **Expresiones booleanas:** evaluación de condiciones como verdadero o falso.
- **Iteración y `any()`:** búsqueda de caracteres que cumplan una condición.
- **Métodos de caracteres:** `.isupper()`, `.islower()` y `.isdigit()`.
- **Módulo estándar `string`:** `string.punctuation` para identificar símbolos de puntuación ASCII.
- **Listas y `sum()`:** suma de comprobaciones booleanas.
- **Condicionales:** `if`, `elif` y `else`.
- **Cadenas formateadas:** uso de f-strings para mostrar resultados.

## Funcionamiento previsto

1. Solicita al usuario una contraseña.
2. Comprueba si tiene al menos ocho caracteres.
3. Comprueba si contiene alguna mayúscula, minúscula, cifra y símbolo incluido en `string.punctuation`.
4. Suma cuántas de esas cinco condiciones se cumplen.
5. Muestra los resultados de las comprobaciones y un mensaje de clasificación.

## Cómo ejecutarlo

Desde la raíz del repositorio:

```bash
python ejercicios/validaciones/password_analyzer.py
```

En algunos sistemas se utiliza `python3` en lugar de `python`. Introduce una contraseña de prueba cuando aparezca el mensaje. **No introduzcas una contraseña personal o real:** el ejercicio muestra en pantalla propiedades de la entrada y no está diseñado para manipular secretos de forma segura.

## Notas de la versión original

Conservo el código exactamente como lo escribí durante mi aprendizaje. En una revisión estática se identificaron las siguientes limitaciones:

- La salida `¿tiene numeros?` imprime `contra_minu` (minúsculas) en lugar de `contra_num` (números). El cálculo de la puntuación sí utiliza `contra_num`.
- La clasificación comprueba primero `seguridad >= 2`; así, puntuaciones de 2, 3, 4 y 5 muestran «nivel bajo». La rama `elif seguridad >= 4` no puede ejecutarse. Con puntuaciones de 0 o 1, el programa muestra «nivel alto».
- El programa comprueba únicamente cinco reglas sencillas; estas reglas no permiten determinar si una contraseña es realmente segura frente a ataques.
- La entrada se solicita mediante `input()`, por lo que los caracteres introducidos pueden ser visibles en la terminal.

Estas notas describen el comportamiento del ejercicio **sin corregir ni reescribir su código**. El valor de este repositorio es mostrar el proceso de aprendizaje y su evolución posterior.

## Alcance

Ejercicio educativo e independiente. El archivo `password_analyzer.py` **no es el módulo `password.py`** utilizado por el [proyecto final de gestión de notas](../../proyectos/sistema_notas/proyecto_final.py).
