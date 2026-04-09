###
# Funciones Input y print
# Como ya conocemos la funcion print nos sirve para presentar mensajes
# La funcion Input sirve para recibir datos de entrada desde la consola
###

nombre = input("Introduce tu nombre\n") # -> la funcion input guarda cadenas de texto

añoNacimiento = int(input("Introduce tu año de nacimiento\n")) # -> convertimos a string para poder operar con eso 

# funcion print sin formateo usamos ',' para poder separar el texto de las variables
# -> la funcion ' sep = "" ' para separar el texto de las variables con un caracter en especifico
# siempre y cuando separemos con comas
# -> la funcion ' end = "" ' para terminar la impresion con algun caracter en especifico
print("Hola" , nombre  , "tienes" , 2026 - añoNacimiento , "años", sep  = "---" , end = "!!\n")
print("***********")

# funcion print con formateo, usamos el caracter 'f' y luego comillas ' f" " ' para 
# poder usar corchetes en los nombres de las variables y que de esa forma
# se pueda colocar el valor de las variables de un solo paso

print(f"Hola {nombre} tienes {2026 - añoNacimiento} años", end = "!!")