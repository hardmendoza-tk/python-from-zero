# Python desde cero 🐍

**Mi primer recorrido aprendiendo Python | Ejercicios originales y proyecto final de Programación I**

Soy **Armando H. Mendoza**, estudiante de Ingeniería en Sistemas. Creé este repositorio para conservar mis primeros ejercicios de programación y documentar cómo fui aprendiendo. El código Python es mi trabajo original: lo mantengo tal como lo escribí, incluso donde existen detalles por mejorar.

> **Enfoque del repositorio:** aprendizaje, evolución y documentación transparente. No pretende presentar los ejercicios iniciales como aplicaciones listas para producción.

## Explora mis trabajos

| Trabajo | Tipo | Qué practiqué | Documentación |
| --- | --- | --- | --- |
| [Analizador de texto](ejercicios/cadenas/analizador_texto.py) | Ejercicio 01 | Cadenas, índices, métodos, ciclos y slicing | [Leer explicación](ejercicios/cadenas/README.md) |
| [Analizador de contraseñas](ejercicios/validaciones/password_analyzer.py) | Ejercicio 02 | Condicionales, `any()`, booleanos y validaciones | [Leer explicación](ejercicios/validaciones/README.md) |
| [Sistema automatizado de gestión de notas](proyectos/sistema_notas/proyecto_final.py) | **Proyecto final — Programación I** | Funciones, listas, diccionarios, menú, estadísticas e importación de módulos | [Documentación técnica](proyectos/sistema_notas/README.md) |

El proyecto final comprende **dos archivos que trabajan juntos**: [`proyecto_final.py`](proyectos/sistema_notas/proyecto_final.py) y [`password.py`](proyectos/sistema_notas/password.py). Este último es su módulo de inicio de sesión demostrativo; **no** es el ejercicio independiente `password_analyzer.py`.

## Estructura del repositorio

```text
python-from-zero/
├── ejercicios/
│   ├── cadenas/
│   │   ├── analizador_texto.py
│   │   └── README.md
│   └── validaciones/
│       ├── password_analyzer.py
│       └── README.md
├── proyectos/
│   └── sistema_notas/
│       ├── proyecto_final.py
│       ├── password.py
│       └── README.md
├── .gitignore
├── LICENSE
└── README.md
```

## Cómo ejecutar los programas

**Requisitos:** Python 3 instalado y una terminal. No se necesitan paquetes externos; se usan herramientas integradas de Python.

Desde la carpeta raíz del repositorio:

**1. Analizador de texto**

```bash
python ejercicios/cadenas/analizador_texto.py
```

**2. Analizador de contraseñas**

```bash
python ejercicios/validaciones/password_analyzer.py
```

**3. Sistema de gestión de notas (proyecto final)**

```bash
python proyectos/sistema_notas/proyecto_final.py
```

En algunas instalaciones debes usar `python3` en vez de `python`. El proyecto final solicita una cuenta de demostración, definida en `password.py`, antes de mostrar su menú. Mantén ambos archivos del proyecto en la misma carpeta para conservar la importación.

## Aprendizajes y alcance

En estos trabajos practiqué:

- Entrada y salida de datos, métodos de cadenas, ciclos y condicionales.
- Funciones y modularización.
- Listas y diccionarios para organizar información.
- Generación de datos ficticios y cálculos estadísticos básicos.
- Construcción de una interfaz de consola mediante menús.
- Importación de funciones desde otro archivo.

### Estado y conservación del código

**Los cuatro archivos `.py` se han conservado byte por byte al reorganizarlos.** Cada trabajo tiene su propia documentación con explicación, instrucciones y limitaciones conocidas.

La revisión realizada fue principalmente **estática**: no afirmo que exista una batería de pruebas automatizadas ni una ejecución integral certificada. Algunas limitaciones conocidas incluyen:

- El analizador de texto puede fallar con entradas vacías.
- El analizador de contraseñas tiene errores originales en una salida y en la clasificación.
- El sistema de notas trabaja con datos ficticios en memoria, sin base de datos.
- Su inicio de sesión es solo didáctico; **no está diseñado para proteger cuentas reales**.

Para entender cada caso, consulta los README individuales enlazados arriba. Mantener estos detalles visibles forma parte de documentar mi progreso de aprendizaje.

## Licencia

Código disponible bajo la [licencia MIT](LICENSE).
