# ¿Qué son las listas en python?🤯
- Es una estructura de datos que permite almacenar una coleccion de elementos.
- A diferencia de las tuplas, las listas son mutables, es decir, son mutables despues de su creación
- Los elementos que se pueden almacenar pueden ser diferentes, es decir, en una lista puede estar almacenado enteros, cadenas de texto, flotantes, etc.

> [!NOTE] 
> ## Creacion de listas
>
> ```python
> # Para crear una lista utilizamos los '[]'
> L1 = [2 , 3 , 4]
> # Tambien podemos almacenar cadenas de texto
> frutas = ['manzana' , 'banana' , 'cereza']
> ```

> [!NOTE] 
> ## Acceso a los elementos
> - Para acceder a sus elementos almacenados, accedemos por el 
> índice(posición).
> - El indice siempre empieza desde el cero
>
> ```python
> # Quiero acceder al valor que se encuentra en la posicion 0
> L1 = [2 , 3 , 4]
> print(L1[0])
> #Salida: 2
> ```

> [!NOTE] 
> ## Modificacion de los elementos
> - Para modificar sus elementos de igual manera accedemos por el indice
>
> ```python
> # Quiero cambiar el valor de la posicion 2
> L1 = [2 , 3 , 4]
> print(L1)
> #Salida: [2, 3, 4]
> 
> L1[2] = 20
> print(L1)
> #Salida: [2, 3, 20]
> ```

> [!NOTE] 
> ## Añadir más elementos
> - Para añadir más elementos usamos la funcion '.append()'
>
> ```python
> # Quiero aniadir mas valores en mi lista 'L1'
> L1 = [2 , 3 , 4]
> print(L1)
> #Salida: [2, 3, 4]
>
> L1.append('David')
> print(L1)
> #Salida: [2, 3, 4, 'David']
> ```