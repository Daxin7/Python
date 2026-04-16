# =============================================================================
# PROYECTO FINAL: EVALUACIÓN ESTUDIANTIL
# =============================================================================

# DESCRIPCIÓN DEL PROYECTO:
# Desarrollar un script simple que solicite al usuario sus notas en tres 
# asignaturas y determine si ha aprobado o reprobado, basándose en el 
# promedio obtenido.

# CARACTERÍSTICAS DEL PROYECTO:
# -----------------------------------------------------------------------------
# 1. ENTRADA DE DATOS: 
#    Solicita al usuario ingresar las notas de tres asignaturas.
#
# 2. CÁLCULO DEL PROMEDIO: 
#    Calcula el promedio de las notas ingresadas.
#
# 3. DETERMINACIÓN DE SITUACIÓN ACADÉMICA: 
#    Utiliza una estructura de control de flujo para determinar si el 
#    estudiante aprueba o reprueba.
#
# 4. FUNCIONES: 
#    Organiza el código utilizando funciones para modularizar la lógica.
#
# 5. CADENAS DE TEXTO: 
#    Forma mensajes sencillos para indicar la situación académica del estudiante.
# -----------------------------------------------------------------------------

def obtenerNotas(): 
    # funcion para obtener las notas
    notas = []
    for i in range(3):
        nota = float(input(f"Ingresa tu nota {i + 1}:\n"))
        notas.append(nota)
    return notas



def calcularPromedio(notas):
    # funcion para calcular el promedio de las notas ingresadas
    return sum(notas) / len(notas)



def determinarSituacionAcademica(promedio):
    # funcion para determinar la situacion academica del estudiante
    if promedio >= 7:
        return "Aprobado"
    else:
        return "Reprobado"

print("Bienvenido al sistema de calificaciones")

notasEstudiante = obtenerNotas()
promedioEstudiante = calcularPromedio(notasEstudiante)
situacionAcademica = determinarSituacionAcademica(promedioEstudiante)

print(f"Tu promedio de notas es: {promedioEstudiante: .2f} y estas {situacionAcademica}")

