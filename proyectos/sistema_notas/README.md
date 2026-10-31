# Sistema automatizado de gestión de notas

**Proyecto final académico — Programación I**  
**Autor:** Armando Harold Mendoza Chuquimia  
**Carrera:** Ingeniería en Sistemas  
**Lenguaje:** Python 3  
**Modalidad:** aplicación de consola

> Esta carpeta conserva el código original presentado como proyecto final. Es una demostración educativa, no un sistema universitario de producción.

## Descripción general

Aplicación de consola que simula la gestión de notas de distintas materias. Permite iniciar sesión, generar materias con docentes y alumnos ficticios, consultar reportes académicos y agregar nuevos estudiantes a una materia durante la ejecución. Los nombres, materias y calificaciones se generan de manera aleatoria.

## Funcionalidades implementadas

- **Inicio de sesión:** usuarios de demostración, comprobación de contraseña mediante un hash SHA-256 y límite de tres intentos por cada llamada de inicio de sesión.
- **Generación de materias:** el usuario indica cuántas materias desea crear; el programa asigna nombres de materia, docentes y estudiantes ficticios.
- **Notas:** calificaciones aleatorias enteras entre 1 y 100.
- **Clasificación por letras:** A (90–100), B (80–89), C (70–79), D (60–69), F (menos de 60).
- **Estado académico:** aprobado desde 51 puntos y reprobado por debajo de 51. La calificación por letra y el estado de aprobación son criterios distintos.
- **Reportes:** consulta de todas las materias o de una en particular, con nombre, nota, letra y estado de cada estudiante.
- **Estadísticas:** nota máxima, mínima, promedio, cantidad de aprobados y reprobados.
- **Gestión de alumnos:** agregar estudiantes generados aleatoriamente a una materia ya registrada.
- **Sesión:** cerrar sesión y volver a la pantalla de autenticación, o salir del programa.

## Archivos y responsabilidades

| Archivo | Responsabilidad |
| --- | --- |
| [`proyecto_final.py`](proyecto_final.py) | Punto de entrada, menú interactivo, generación de datos, gestión de materias y alumnos, cálculo de notas y reportes. |
| [`password.py`](password.py) | Módulo de inicio de sesión: usuarios de prueba, hashes de contraseña, verificación y control de intentos. |

La línea `from password import fIniciarSesion` del programa principal requiere que ambos archivos permanezcan en esta misma carpeta.

## Arquitectura y flujo

```text
proyecto_final.py
    |
    +--> password.py: fIniciarSesion()
    |       +--> validar usuario y contraseña
    |       +--> permitir acceso o terminar tras 3 intentos
    |
    +--> fMenuNotas()
            +--> 1. Generar materias ficticias
            +--> 2. Mostrar reportes de todas las materias
            +--> 3. Mostrar reporte de una materia
            +--> 4. Agregar estudiantes ficticios
            +--> 5. Cerrar sesión
            +--> 6. Salir
```

El programa comienza en `pMain()`, que llama a `fIniciarSesion()` y, tras autenticarse, a `fMenuNotas()`.

## Estructuras de datos y lógica

Se utilizan **listas** y **diccionarios** de Python. El registro `aRegistroMaterias` contiene los datos de las materias creadas durante la sesión. Cada materia incluye un nombre, un docente y una lista de estudiantes. Cada estudiante se representa mediante un diccionario con estos campos:

```python
{
    "Nombre_Completo": "Estudiante de ejemplo",
    "Nota": 85,
    "Letra": "B",
    "Estado": "APROBADO"
}
```

Este bloque es un **ejemplo ilustrativo de la estructura**, no un registro fijo guardado por la aplicación.

Para generar datos se emplean `random.choice()` y `random.randint()`. Para calcular estadísticas, `max()`, `min()`, `sum()` y `len()`. El código separa tareas en funciones, como `fGenerarNotas()`, `fObtenerLetra()`, `fLlenarEstudiantes()` y `pImprimirReporteMateria()`.

## Requisitos y ejecución

- Python 3 instalado.
- Terminal o consola.
- Sin dependencias externas: se utilizan únicamente `random` y `hashlib`, de la biblioteca estándar.

Desde la **raíz de `python-from-zero`**:

```bash
python proyectos/sistema_notas/proyecto_final.py
```

En sistemas donde corresponda, utiliza `python3` en lugar de `python`.

Para probar únicamente la pantalla de inicio de sesión:

```bash
python proyectos/sistema_notas/password.py
```

### Recorrido de demostración

1. Iniciar el programa y autenticarse con uno de los usuarios de demostración definidos en `password.py`.
2. Seleccionar **1** y generar una o más materias con estudiantes ficticios.
3. Seleccionar **2** para visualizar los reportes y las estadísticas.
4. Seleccionar **3** para consultar una materia concreta.
5. Seleccionar **4** para añadir estudiantes ficticios a una materia.
6. Utilizar **5** para cerrar sesión o **6** para salir.

Los usuarios y hashes de demostración están incluidos en el código original para fines educativos. **No reutilices estas credenciales para cuentas o servicios reales.**

## Principales conceptos puestos en práctica

- Programación estructurada y modularización mediante funciones.
- Colecciones: listas y diccionarios.
- Condicionales, ciclos `while` y `for`, y menús interactivos.
- Validación de entradas numéricas mediante `try/except ValueError`.
- Generación de datos de prueba con `random`.
- Cálculo de estadísticas básicas y presentación de reportes tabulares.
- Separación de responsabilidades mediante importación de funciones de otro archivo.
- Introducción a hashing con `hashlib` y control de intentos.

## Alcance y limitaciones de la versión original

Este repositorio conserva los archivos **sin modificar su lógica ni su contenido**. A partir de la revisión estática del código:

- **Persistencia:** las materias y notas residen en memoria; se pierden al terminar el programa. No hay archivos de datos ni base de datos.
- **Datos ficticios:** estudiantes, docentes, materias y notas se generan aleatoriamente; no se cargan expedientes reales.
- **Credenciales de demostración:** se almacenan hashes SHA-256 sin sal individual ni una función de derivación de claves apropiada para contraseñas. Además, las contraseñas de ejemplo son débiles y la entrada con `input()` es visible en pantalla. El módulo **no debe utilizarse para autenticar usuarios reales**.
- **Control de acceso:** el usuario autenticado abre el mismo menú general; no existe autorización diferenciada por rol.
- **Límite de intentos:** se aplica por ejecución de la función de inicio de sesión, sin bloqueos persistentes.
- **Reportes:** la función `pImprimirReportePorPartes()` existe en el código, pero no está expuesta en el menú principal.
- **Criterios de nota:** una nota entre 51 y 59 figura como `F`, pero su estado es `APROBADO`, de acuerdo con las reglas implementadas; la documentación refleja este comportamiento sin corregirlo.
- **Pruebas:** la descripción anterior se basa en la lectura del código; todavía no se han ejecutado pruebas integrales ni automatizadas en este proceso de documentación.

## Propósito académico

Este proyecto reúne lo aprendido durante Programación I en un ejercicio de mayor alcance que los programas iniciales: integra varias funciones, datos estructurados, interacción por consola, un módulo separado y reportes.

**Criterio de conservación:** la implementación Python se mantiene tal como fue escrita originalmente, como evidencia del aprendizaje y punto de partida para futuros proyectos.

## Licencia

Consulta la [licencia MIT del repositorio](../../LICENSE).
