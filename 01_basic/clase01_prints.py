# una variable es un contenedor que almacena un valor
saludo = "Hola" # -> cadena de string
nombre = "David" # -> cadena de string 
apellido = "Jacome" # -> cadena de string
nombreCompleto = nombre +  " " + apellido
print("***********************") # -> con doble comilla para texto
print(saludo, nombre, apellido) # -> separado por defecto
print(saludo, nombre, apellido, sep = "-") # -> con el 'sep' le damos el parametro por el cual van a estar separadas la palabras 

print("\n")
print('***********************') # -> con comilla simple tambien funciona

print(nombreCompleto)
print(type(saludo)) # -> funcion para imprimir el tipo de dato de una variable 

