###
# Operadores aritméticos y de comparación
# para realizar calculos basicos y apra evaluar condiciones
###


# OPERADORES DE CALCULOS (+ , - , * , / , %)
print(5 + 4)
print(5 - 1)
print(3 * 4)
print(8 / 2)
print(5 % 2) # -> modulo: residuo de una division
print(5 // 2) # -> división entera o floor division. Este operador divide dos números y redondea el resultado hacia abajo al número entero más cercano
print(5 ** 2)
print(5 ** 2)

print("===========")

# OPERADORES DE COMPARACION (sirve para evaluar condicioones)
5 == 5 # -> '=='  -  'es igual a
5 != 5 # -> '!='  -  'es distinto de'
5 > 5 # -> '>'  -  'es mayor que'
5 < 5 # -> '<'  -  'es menor que'
5 >= 5 # -> '>='  -  'mayor o igual que'
5 <= 5 # -> '<='  -  'menor o igual que'

print("===========")

# OPERADORES LOGICOS (AND , OR , NOT)

#ejemplo 1

edad = 18
tiene_experiencia = True

if edad > 18 and tiene_experiencia: # -> Aqui usamos el operador AND para evaluar condicnoes, si todas las condicioens son verdaderas, el resultado es verdadero
    print("Es apto para trabajar en la empresa")
else:
    print("No es apto para trabajar en la empresa")

print("***********")

#ejemplo2

es_estudiante = False
es_profesor = False

if es_estudiante or es_profesor: # -> Aqui usamor el operador OR para evaluar condiciones, si alguna de las condiciones es verdadera, el resultado es verdadero
    print("La persona es estudiante o es profesor")
else:
    print("La persona no es ninguno de los dos")

print("***********")

#ejemplo3

llueve = False

if not llueve: # -> Aqui usamos el operador NOT para cambiar el valor de verdad de la condicion
    print("No esta lloviendo")
else:
    print("Esta lloviendo")