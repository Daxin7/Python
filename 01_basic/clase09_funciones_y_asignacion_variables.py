###
# FUNCIONES
# Son un bloque de código que lo podemos reutilizar más adelante
# estos bloques de código pueden depender de ciertos parámetros o no
# Ademas, las funciones no siempre tendran que retornar un valor
###

### SINTÁXIS
# -> la palabra 'def' es para crear la funcion, 
# luego va el nombre de la funcion y lo que va dentro 
# del parentesis son los parametros de los cuales depende la funcion
# IMPORTANTE:
# Si una funcion no lleva parametros se les denominan funcniones anonimas
def mi_funcion(parametro1 , parametro2): 
    # cuerpo de la funcion
    resultado = parametro1 + parametro2
    return resultado

print(mi_funcion(3 , 5)) #-> de esta manera hacemos uso de la funcion


print("**********")
# otro ejemplo

def Saludar(saludo, nombre):
    print(f"{saludo} {nombre}!")

print(Saludar("Hola" , "David"))
print("**********")

# tambien podemos predefinir los valores de los parametros en la funcion
def Saludar1(nombre, saludo1="HOLA"):
    print(f"{saludo1} , {nombre}")

print(Saludar1("DAVID"))
print("**********")

# otro ejemplo de funcion
def cuadrado(x):
    result = x ** 2
    return result

print(cuadrado(4))
print("**********")

# Ejemplos de funcniones anonimas

def Imprimir():
    print("Hola Mundo!")

resultado = Imprimir()

print(resultado)#-> aqui imprime None ya que la funcion Imprimir no retorna ningun valor

print("**********")