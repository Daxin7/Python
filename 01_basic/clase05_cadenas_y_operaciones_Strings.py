
sopa = "Colada de haba"
conector = ' y '
segundo = "Camarones apanados"
todo = sopa + conector + segundo
print(sopa + conector + segundo) # -> concatenar cadenas de texto

print("*********")

print(sopa[1]) # -> pedir posicion de una cadena (OJO...empieza desde el cero la posicion)

print("*********")

print(sopa[0:3]) # -> pedir un intervalo de caracteres en una cadena

print("*********")

print(len(sopa)) # -> pedir el tamanio de una cadena de texto (OJO... aqui si empieza desde uno)

print("*********")

print(sopa[-1]) # -> para obtener el ultimo caracter de una cadena sin tener que saber cuantos caracteres son

print("*********")

print(sopa[-5:-1]) # -> tambien funciona como intervalo

print("*********")

print(sopa.upper()) # -> para convertir a mayusculas

print("*********")

print(sopa.lower()) # -> para convertir a minusculas

print("*********")

print("david".upper())

print("*********")

print("david".capitalize()) # -> para poner el primer caracter en mayuscula

print(todo.split()) # -> para convertir a lista (Borra los espacios y toma como elemento cada cadena de texto)