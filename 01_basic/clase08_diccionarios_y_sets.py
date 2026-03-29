###
#En Python, un diccionario es una estructura de datos que almacena pares clave–valor.
#Es muy útil cuando necesitas acceder a datos por una clave en lugar de un índice numérico (como en las listas).
# la clave debe ser unica para cada valor. Los diccionarios se los coloca entre llaves
###


mi_diccionario = {"clave1": 2 , "clave2" : 4 , "clave3" : 6 }

valor = mi_diccionario["clave1"]

print(mi_diccionario["clave1"]) # aqui imprimos el valor de 'clave1' y como podemos ver no se usa parentesis, sino, corchetes haciendo alusion a la posicion por asi decirlo
print(valor) # otra forma de imprimir el valor de un diccionario mediante su clave

print("**********")

# lo que podemos hacer con los diccionarios es modificar los valores
mi_diccionario["clave1"] = 8

print(mi_diccionario["clave1"])

print(mi_diccionario) # imprimir todo el diccionario

print("**********")

# para eliminar un valor con su calve, usamos la funncion .pop()

# imprimimos de nuevo el diccionario
print(mi_diccionario)
mi_diccionario.pop("clave3") # -> eliminamos el valor que tiene 'clave3' con la funcion '.pop()'

# volvemos a imprimir el diccionario
print(mi_diccionario)

print("**********")

#imprimir el diccionario con clave y valor
for key , value in mi_diccionario.items(): #-> la funcion .items() sirve para obtener una vista iterable de sus pares clave–valor.
    print(f"La clave es {key} y su valor es {value}")

print("**********")

# imprimir el diccionario solo con las claves

for elemento in mi_diccionario:
    print(elemento)

print("**********")

print(mi_diccionario.keys())# -> '.keys()' para imprimir sus claves en forma de lista

print(mi_diccionario.values()) # -> '.values()' para imprimir sus valores en forma de lista

print(mi_diccionario.items()) # -> '.items()' para imprimir clave-valor en forma de tuplas

print("**********")

##  Conjuntos -> una cosa importante de los conjuntos es que no se puden repetir los valores. Los conjuntos se los coloca entre llaves

mi_set = {1 , 2 , 3} # -> declaramos un conjunto 

print(mi_set) # -> imprimimos el conjunto 

print("**********")

mi_set1 = {1 , 2 , 3 , 3} # -> declaramos otro conjunto pero con un caracter repetido

print(mi_set1) # -> volvemos a imprimir y veremos que no se imprime dos veces el '3'

print("**********")

## OPERACIONES CON CONJUNTOS
mi_set2 = {1 , 2 , 3}
mi_set3 = {3 , 4 , 6}

# union de conjuntos
print(mi_set2 | mi_set3) 
print("**********")

# interseccion de conjuntos
print(mi_set2 & mi_set3)
print("**********")

