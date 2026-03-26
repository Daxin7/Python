# CONDICIONALES (if , elif , else)

#ejemplo1
'''
Determinar si un numero es par o impar
'''
num1 = 124

if num1 % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("***********")

#ejemplo2
'''
Validar el signo de un numero
'''

num2 = 9

if num2 > 0:
    print("El numero es positivo")
elif num2 == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")

print("============")

###
# MATCH , CASE -> Es una estructura de control condicional
###

#ejemplo1
opcion = 3

match opcion:
    case 1:
        print("Opcion vegana")
    case 2:
        print("Opcion carnivora")
    case 3:
        print("Opcion mixta")

print("***********")

#ejemplo2

numero = 30
match numero:
    case 0:
        print("El numero es cero")
    case n if n > 0:
        print("El numero es positivo")
    case n if n < 0:
        print("El numero es negativo")
    case _:
        print("No se puede clasificar la imagen")