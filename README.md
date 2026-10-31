# Python desde cero 🐍

Repositorio de aprendizaje de Python de Armando H. Mendoza, estudiante de Ingeniería en Sistemas. Reúne ejercicios de programación y un proyecto académico de gestión de notas.

## Contenido

| Ruta | Descripción |
| --- | --- |
| [`ejercicios/cadenas/analizador_texto.py`](ejercicios/cadenas/analizador_texto.py) | Operaciones con cadenas: mayúsculas, minúsculas, palabras, inversión y sustitución de vocales. |
| [`ejercicios/validaciones/password_analyzer.py`](ejercicios/validaciones/password_analyzer.py) | Ejercicio de comprobación de características de una contraseña. |
| [`proyectos/sistema_notas/proyecto_final.py`](proyectos/sistema_notas/proyecto_final.py) | Proyecto académico de gestión de notas con menú, generación de registros y reportes. |
| [`proyectos/sistema_notas/password.py`](proyectos/sistema_notas/password.py) | Módulo de inicio de sesión empleado por el proyecto de notas. |

## Requisitos

- Python 3 (se recomienda una versión reciente).
- No se requieren paquetes de terceros: los scripts emplean módulos estándar de Python.

## Cómo ejecutar

Desde la carpeta raíz del repositorio, abre una terminal y ejecuta el programa que te interese.

**Analizador de texto:**

```bash
python ejercicios/cadenas/analizador_texto.py
```

**Analizador de contraseñas:**

```bash
python ejercicios/validaciones/password_analyzer.py
```

**Sistema académico de notas:**

```bash
python proyectos/sistema_notas/proyecto_final.py
```

El sistema de notas requiere que `password.py` permanezca en la misma carpeta que `proyecto_final.py`. Solicita credenciales de demostración antes de presentar el menú.

> En algunos sistemas, el comando para ejecutar Python es `python3` en lugar de `python`.

## Estado y limitaciones conocidas

Los cuatro archivos Python fueron reorganizados sin modificar su contenido original. Las siguientes observaciones provienen de la **revisión estática del código**; no constituyen pruebas completas de ejecución.

- **Analizador de texto:** una entrada vacía o solo con espacios puede generar un `IndexError`.
- **Analizador de contraseñas:** la línea que muestra si hay números utiliza la variable de minúsculas, y las condiciones para clasificar la seguridad están ordenadas incorrectamente.
- **Inicio de sesión:** las contraseñas de ejemplo son débiles y sus hashes SHA-256 no incorporan sal ni un algoritmo especializado para almacenamiento seguro de contraseñas. Es exclusivamente un ejercicio académico, no un sistema de autenticación para producción.
- **Sistema de notas:** genera datos aleatorios y los conserva en memoria durante la ejecución; no cuenta con persistencia en base de datos.
- **Pruebas:** ejecución integral y casos de prueba automatizados pendientes de completar.

## Objetivo de aprendizaje

Practicar fundamentos de Python, control de flujo, cadenas, funciones, listas, diccionarios, importaciones entre módulos y organización de proyectos. Este repositorio documenta mi progreso y las mejoras posteriores.

## Licencia

Este repositorio se distribuye bajo la [licencia MIT](LICENSE).
