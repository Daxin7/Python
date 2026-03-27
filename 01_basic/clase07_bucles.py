###
# For , BREAK , CONTINUE
# los bucles sirven para 
# repetir un bloque de código varias veces de forma automática, 
# sin tener que escribir las mismas instrucciones una y otra vez.
###

#ejemplo1
secuencia = [1 , 2 , 3 , 4 , 5]
for elemento in secuencia:
    print(elemento)

print("********")

#ejemplo2
for letra in "Python":
    print(letra)

print("********")

#ejemplo3
for x in range(5):
   print(x)

print("********")

#ejemplo4

for y in range(len(secuencia)):
    print(y)

print("********")

#ejemplo5

for indice, valor in enumerate(secuencia): # -> la funcion enumerate sirve para iterar sobre una secuencia (lista, tupla, cadena, etc.) obteniendo al mismo tiempo el índice y el valor de cada elemento.
    print(f"Elemento {indice} : {valor}") # -> aqui el caracter 'f' es para reemplazar los valores que indicamos en el for, y los ponemos entre llaves para ser reemplazados

print("********")

#ejemplo6
for elemento in secuencia:
    print(elemento)
    if elemento == 3:
        break # -> el break lo que hace es matar el bucle hasta que una condicion sea verdadera

print("********")

#ejemplo7
for elemento in secuencia:
    if elemento == 3:
        continue # -> el continue hace que se salte la iteracion del bucle segun la condicion dada
    print(elemento)

print("============")

###
# BUCLE WHILE
# -> sirve para ejecutar un bloque de codigo mientras una condicion sea verdadera
###

#ejemplo1

contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1 # esta es una asignacion, es decir va a saumar 1 a contador y luego va a actualizar su valor

print("********")

#ejemplo2
contador = 0
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador == 5:
        break