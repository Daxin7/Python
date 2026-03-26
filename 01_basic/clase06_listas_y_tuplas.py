###
# Las listas y las tuplas son un tipo de estructuras de datos
# pueden almacenar diferentes tipos de datos
# podemos llamar a los datos segun su posicion
#
# LA DIFERENCIA ES QUE EN LISTAS PODEMOS CAMBIAR DATOS
# EN CAMBIO, EN TUPLAS LOS DATOS NO PUEDEN SER MODIFICADOS
###

# Esto es lista ( CON CORCHETES ' [] ')
mi_lista = [1 , 2 , 3 , "David" , True]

# Esto es tupla ( CON PARENTESIS ' () ')
mi_tupla = (1 , 2 , 3 , "David" , True)

print("**********")

print(mi_lista[0]) # -> las listas tambien comienzan desde el cero

print("**********")

mi_lista[0] = 24

print(mi_lista) # -> aqui podemos ver que ya cambio

# lo que podemos hacer con listas es tambien insertar mas datos

print("**********")

mi_lista.append("Jacome") # -> para aniadir mas items
print(mi_lista)

print("**********")

print(len(mi_lista)) # -> para imprimir cuantos items tiene la lista

print("**********")

print(len(mi_tupla)) # -> para imprimir cuantos items tiene la tupla

# lo que tambien se puede hacer es remover elementos

print("**********")

mi_lista.remove(True)
print(mi_lista)

