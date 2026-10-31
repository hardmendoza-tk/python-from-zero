"""             ESTUDIANTE: Armando Harold Mendoza Chuquimia
                CARRERA: Ingenieria en Sistemas
                Materia: Programacion 1
                Tema Proyecto: Notas Automatizadas"""

import random #Importamo la libreria random
from password import fIniciarSesion #Importamos 
# Marcador de autenticidad: X7K9
__codigo_original__ = True 
aRegistroMaterias = [] # Listas de datos base
aNombres = [
    "Ana", "Luis", "Carlos", "María", "Sofía",
    "Pedro", "Laura", "Miguel", "Elena", "Jorge",
    "Andrés", "Lucía", "Diego", "Carmen", "Roberto",
    "Patricia", "Fernando", "Rosa", "Daniel", "Isabel"
]
aApellidos = [
    "García", "López", "Martínez", "Hernández", "Pérez",
    "Sánchez", "Ramírez", "Torres", "Flores", "Rivera",
    "Morales", "Ortiz", "Guzmán", "Moreno", "Romero",
    "Herrera", "Medina", "Castro", "Vargas", "Jiménez"
]
aMaterias = [
    "Fundamentos de Matemáticas", "Inglés Técnico I", "Programación Básica", "Hardware, Software y Redes",
    "Estructuras Discretas", "Cálculo I", "Ética y Ciudadanía Global", "Álgebra Lineal", "Física I",
    "Programación I", "Cálculo II", "Gestión Financiera para Proyectos TIC", "Programación II",
    "Sistemas Operativos II", "Física II", "Investigación Operativa I", "Redes I", "Análisis Numérico",
    "Programación III", "Base de Datos I"
]
aProfesiones = [
    "Ing.", "Lic.",
    "Doc.", "Mtr."
]

# FUNCIONES PARA GENERAR DATOS
def fGenerarNotas():
    return random.randint(1, 100)
def fSacarNombreCompleto():
    sNombre = random.choice(aNombres)
    sApellido = random.choice(aApellidos)
    return sNombre + " " + sApellido
def fSacarDocente():
    sNombre = fSacarNombreCompleto()
    sProfesion = random.choice(aProfesiones)
    return sProfesion + " " + sNombre
def fSacarMateria():
    return random.choice(aMaterias)
# FUNCIONES PARA CLASIFICAR NOTAS
def fObtenerLetra(nNota):
    if nNota >= 90:
        sLetra = "A"
    elif nNota >= 80:
        sLetra = "B"
    elif nNota >= 70:
        sLetra = "C"
    elif nNota >= 60:
        sLetra = "D"
    else:
        sLetra = "F"
    return sLetra

def fObtenerEstadoNota(nNota):
    if nNota >= 51:
        sEstado = "APROBADO"
    else:
        sEstado = "REPROBADO"
    return sEstado
def fNotaMaxima(aLista):
    return max(aLista)
def fNotaMinima(aLista):
    return min(aLista)
def fPromedio(aLista):
    return sum(aLista) / len(aLista)

# FUNCIONES PARA ALUMNOS
def pAgregarAlumno(aLista, sNombreCompleto, nNota):
    sLetra = fObtenerLetra(nNota)
    sEstado = fObtenerEstadoNota(nNota)
    dAlumno = {
        "Nombre_Completo": sNombreCompleto,
        "Nota": nNota,
        "Letra": sLetra,
        "Estado": sEstado
    }
    aLista.append(dAlumno)

def fLlenarEstudiantes(nCantidad):
    aListaAlumnos = []
    for _ in range(nCantidad):
        sNombreCompleto = fSacarNombreCompleto()
        nNota = fGenerarNotas()
        pAgregarAlumno(
            aListaAlumnos,
            sNombreCompleto,
            nNota
        )
    return aListaAlumnos

# FUNCIONES PARA REPORTES
def fCalcularAnchoColumnaNombre(aListaEstudiantes):
    nMaxLongitud = 0
    for dEstudiante in aListaEstudiantes:
        if len(dEstudiante["Nombre_Completo"]) > nMaxLongitud:
            nMaxLongitud = len(dEstudiante["Nombre_Completo"])
    return max(nMaxLongitud, 15)

def pImprimirTablaEstudiantes(aListaEstudiantes, nLongitudNombre):
    print(
        f"{'ID':<4} "
        f"{'Nombre Completo':<{nLongitudNombre}} "
        f"{'Nota':<5} "
        f"{'Letra':<5} "
        f"{'Estado':<10}"
    )
    print("-" * (4 + 1 + nLongitudNombre + 1 + 5 + 1 + 5 + 1 + 10))
    for iIndice, dEstudiante in enumerate(aListaEstudiantes):
        print(
            f"{iIndice + 1:<4} "
            f"{dEstudiante['Nombre_Completo']:<{nLongitudNombre}} "
            f"{dEstudiante['Nota']:<5} "
            f"{dEstudiante['Letra']:<5} "
            f"{dEstudiante['Estado']:<10}"
        )
def pImprimirResumenEstadistico(aListaEstudiantes, nLongitudNombre):
    aNotas = [
        dEstudiante["Nota"]
        for dEstudiante in aListaEstudiantes
    ]
    print("-" * (4 + 1 + nLongitudNombre + 1 + 5))
    print("--- Estadísticas Generales ---")
    print(f"Nota Máxima: {fNotaMaxima(aNotas)}")
    print(f"Nota Mínima: {fNotaMinima(aNotas)}")
    print(f"Promedio:    {fPromedio(aNotas):.2f}")
    sEstadoGrupo = fObtenerEstadoNota(fPromedio(aNotas))
    print(f"Estado grupo: {sEstadoGrupo}")
    nAprobados = 0
    nReprobados = 0
    for dEstudiante in aListaEstudiantes:
        if dEstudiante["Estado"] == "APROBADO":
            nAprobados += 1
        else:
            nReprobados += 1
    print(f"Aprobados: {nAprobados}")
    print(f"Reprobados: {nReprobados}")
def pImprimirReporteMateria(sNombreMateria, dDatos):
    sDocente = dDatos["docente"]
    aListaEstudiantes = dDatos["estudiantes"]
    print(f"\nMATERIA: {sNombreMateria}")
    print(f"DOCENTE: {sDocente}")
    if not aListaEstudiantes:
        print("No hay estudiantes registrados en esta materia.")
        return
    nLongitudNombre = fCalcularAnchoColumnaNombre(aListaEstudiantes)
    pImprimirTablaEstudiantes(aListaEstudiantes, nLongitudNombre)
    pImprimirResumenEstadistico(aListaEstudiantes, nLongitudNombre)

def pImprimirReportePorPartes(aMateriasCargadas):
    if not aMateriasCargadas:
        print("\n[!] No hay materias ni notas registradas aún.")
        return
    print("\n" + "=" * 50)
    print("      REPORTE POR MATERIA (PASO A PASO)")
    print("=" * 50)
    nTotalMaterias = len(aMateriasCargadas)
    for iIndice, dMateriaActual in enumerate(aMateriasCargadas, 1):
        print(f"\n[ Materia {iIndice} de {nTotalMaterias} ]")
        pImprimirReporteMateria(dMateriaActual["nombre"], dMateriaActual)
        if iIndice < nTotalMaterias:
            input("\n---> Presione [Enter] para continuar...")
def pImprimirReporteFinal(aMateriasCargadas):
    if not aMateriasCargadas:
        print("\n[!] No hay materias ni notas registradas aún.")
        return
    print("\n" + "=" * 50)
    print("         REPORTE FINAL")
    print("=" * 50)
    for dDatos in aMateriasCargadas:
        pImprimirReporteMateria(dDatos["nombre"], dDatos)
# FUNCIONES PARA MATERIAS

def fCapturarDatosMateria(iIndice, nTotal):
    print(
        f"\n--- Materia {iIndice + 1} de {nTotal} ---"
    )
    sNombreMateria = fSacarMateria()
    sDocente = fSacarDocente()
    print(
        "MATERIA SELECCIONADA:",
        sNombreMateria
    )
    print(
        "DOCENTE ASIGNADO:",
        sDocente
    )
    while True:
        try:
            nCantidadAlumnos = int(
                input(
                    "Ingrese la cantidad de alumnos: "
                )
            )
            if nCantidadAlumnos < 0:
                print(
                    "La cantidad de alumnos no puede ser negativa."
                )
            else:
                break
        except ValueError:
            print(
                "Ingrese un número válido."
            )
    return {
        "nombre": sNombreMateria,
        "docente": sDocente,
        "estudiantes": fLlenarEstudiantes(nCantidadAlumnos)
    }
def fCantidadMaterias(nCantidad):
    aMateriasCargadas = []
    for iIndice in range(nCantidad):
        dDatosMateria = fCapturarDatosMateria(iIndice, nCantidad)
        aMateriasCargadas.append(dDatosMateria)
    return aMateriasCargadas
def pMenuInteractivo():
    while True:
        try:
            nCantidad = int(input("Ingrese la cantidad de materias: "))
            if nCantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Ingrese un número válido.")
    aNuevasMaterias = fCantidadMaterias(nCantidad)
    aRegistroMaterias.extend(aNuevasMaterias)

# SELECCIONAR MATERIA
def fSeleccionarMateriaExistente():
    if not aRegistroMaterias:
        print(
            "\n[!] No hay materias registradas."
        )
        return None
    print("\n--- MATERIAS REGISTRADAS ---")
    for iIndice, dDatos in enumerate(
        aRegistroMaterias,
        1
    ):
        print(f"{iIndice}.- {dDatos['nombre']}")
    while True:
        try:
            nOpcion = int(input("\nSeleccione el número de la materia: "))
            if 1 <= nOpcion <= len(aRegistroMaterias):
                return aRegistroMaterias[nOpcion - 1]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Ingrese un número entero.")

# AGREGAR ESTUDIANTES
def pAgregarEstudiantesAMateria():
    dMateriaSeleccionada = fSeleccionarMateriaExistente()
    if dMateriaSeleccionada is None:
        return
    print(
        f"\nMateria elegida: "
        f"{dMateriaSeleccionada['nombre']}"
    )
    try:
        nCantidadNuevos = int(
            input(
                "Ingrese la cantidad de nuevos alumnos: "
            )
        )
        if nCantidadNuevos <= 0:
            print(
                "La cantidad debe ser mayor a 0."
            )
            return
        aNuevosAlumnos = fLlenarEstudiantes(
            nCantidadNuevos
        )
        dMateriaSeleccionada["estudiantes"].extend(
            aNuevosAlumnos)
        print(
            f"\n[✓] Se añadieron "
            f"{nCantidadNuevos} nuevos estudiantes."
        )
    except ValueError:
        print("Entrada inválida.")

# MENÚ
def fMostrarMenu():
    sMenu = """
========================================
        SISTEMA DE GESTIÓN DE NOTAS
========================================

1.- Generar materias aleatorias
2.- Imprimir todas las materias
3.- Imprimir una materia
4.- Agregar alumnos a una materia
5.- Cerrar sesión
6.- Salir del programa

Seleccione una opción:
"""
    return sMenu
# MENÚ DE NOTAS
def fMenuNotas():
    while True:
        sOpciones = input(fMostrarMenu())
        if sOpciones == "1":
            pMenuInteractivo()
        elif sOpciones == "2":
            pImprimirReporteFinal(aRegistroMaterias)
        elif sOpciones == "3":
            dMateriaSeleccionada = fSeleccionarMateriaExistente()
            if dMateriaSeleccionada is not None:
                pImprimirReporteMateria(dMateriaSeleccionada["nombre"], dMateriaSeleccionada)
        elif sOpciones == "4":
            pAgregarEstudiantesAMateria()
        elif sOpciones == "5":
            print(
                "\nCerrando sesión..."
            )
            return "cerrar_sesion"
        elif sOpciones == "6":
            print(
                "\nSaliendo del programa..."
            )
            return "salir"
        else:
            print(
                "\nOpción no válida. " 
                "Seleccione una opción del 1 al 6.")

# PROGRAMA PRINCIPAL
def pMain():
    while True:
        bAcceso = fIniciarSesion()
        if not bAcceso:
            return
        sResultado = fMenuNotas()
        if sResultado == "salir":
            return
        if sResultado == "cerrar_sesion":
            print("\nSesión cerrada.")
            print("Volviendo al inicio de sesión...")

#Funcio para la ejecucion del programa
if __name__ == "__main__":
    pMain()