###
# Para crear una lista usamos los '[]'
###
L1 = [2 , 3 , 4]
print(L1)
print("********")

# Tambien podemos almacenar cadenas de texto
frutas = ['manzana' , 'banana' , 'cereza']
print(frutas)
print("*********")

###
# Para acceder a sus elementos usamos el indice(posicion)
###

# Quiero acceder al valor que se encuentra en la posicion 0
L1 = [2 , 3 , 4]
print(L1[0])

print("*********")

###
#  Modificacion de los elementos
###

# -> Para modificar sus elementos de igual manera accedemos por el indice

# Quiero cambiar el valor de la posicion 2 de L1
L1 = [2 , 3 , 4]
print(L1)

L1[2] = 20
print(L1)
print("*********")

### 
# Añadir más elementos
###

# -> Para añadir más elementos usamos la funcion '.append()'
# Quiero aniadir mas valores en mi lista 'L1', entonces usamos '.append()'
# La funcion '.append()' aniade los elmentos al final de la lista
L1 = [2 , 3 , 4]
print(L1)

L1.append('David')
print(L1)
print("**********")

###
# Insertar elementos en una posición en específico
###
# Para añadir más elementos en una posición en específico usamos la función '.insert('indice', 'valor')' .
# Quiero aniadir mas valores en mi lista 'L1' en la posicion 2
L1 = [2 , 3 , 4]
print(L1)


L1.insert(2, 25)
print(L1)
#Salida: [2, 3, 25, 4]
print("*******")

###
# Eliminar elementos de una lista
# Para eliminar los elementos en una lista usamos el método '.remove()'
# El método '.remove()' elimina la primera aparición del valor que le pasemos como parámetro

# Quiero remover el valor de 2
L1 = [2 , 2, 3 , 4]
print(L1)

L1.remove(2)
print(L1)
print("*********")

###
# Eliminar elemento segun la posición
#
# Para eliminar un elemento segun la posicion usamos el metodo 'del'

# Quiero remover el valor de la posicion 1
L1 = [2, 3 , 4]
print(L1)

del L1[1] #-> Aqui le pasamos la posicion del valor
print(L1)
print("********")

###
# Eliminar ultimo elemento de una lista
###
# Para eliminar el ultimo elemento de una lista, usamos el método '.pop()'

# Quiero remover el ultimo elemento de la lista
L1 = [2, 3 , 4]
print(L1)
#Salida: [2, 3, 4]

L1.pop()
print(L1)
print("*********")

###
# Longitud de una lista
# Para conocer la longitud de una lista, usamos el método 'len('nombre de la lista')'

# Quiero conocer la longitud de L1
L1 = [2, 3 , 4]
print(L1)
#Salida: [2, 3, 4]

print(len(L1))
print("*********")

###
# Imprimir los elementos de una lista
###
# Para imprimir los elementos de una lista usamos un bucle 'for'

# Quiero imprimir los elementos de L1
L1 = [2, 3 , 4]
for i in L1:
    print(i)    
print("********")

### 
# Transformar una cadena de caracteres a lista
###
# Para transformar una cadena de caracteres en una lista, usamos el metodo 'list()'

# Quiero transformar la cadena de caracteres de la variable palabra
palabra = "David"
conversion = list(palabra)    
print(conversion)