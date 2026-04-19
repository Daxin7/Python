# ¿Qué son las listas en python?🤯
- Es una estructura de datos que permite almacenar una colección de elementos.
- A diferencia de las tuplas, las listas son mutables después de su creación.
- Los elementos que se pueden almacenar pueden ser diferentes, es decir, en una lista puede estar almacenado enteros, cadenas de texto, flotantes, etc.

> [!NOTE] 
> ## Creación de listas
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
> ## Modificación de los elementos
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
> - Para añadir más elementos usamos el método '.append()' .
> - El método '.append()' añade elementos al final de la lista.
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

> [!NOTE] 
> ## Insertar elementos en una posición en específico
> - Para añadir más elementos en una posición en específico usamos el método '.insert('indice', 'valor')' .
>
> ```python
> # Quiero añadir mas valores en mi lista 'L1' en la posicion 2
> L1 = [2 , 3 , 4]
> print(L1)
> #Salida: [2, 3, 4]
>
> L1.insert(2, 25)
> print(L1)
> #Salida: [2, 3, 25, 4]
> ```

> [!NOTE] 
> ## Eliminar elemento de una lista
> - Para eliminar los elementos en una lista usamos el método '.remove()'
> - El método '.remove()' elimina la primera aparición del valor que le pasemos como parámetro
> - Si el valor no está en la lista, aparecera un error 'ValueError'.
>
> ```python
> # Quiero remover el valor de 2
> L1 = [2 , 2, 3 , 4]
> print(L1)
> #Salida: [2, 2, 3, 4]
>
> L1.remove(2)
> print(L1)
> #Salida: [2, 3, 4]
> ```

> [!NOTE] 
> ## Eliminar elemento según la posición
> - Para eliminar un elemento segun la posicion usamos el método 'del'
>
> ```python
> # Quiero remover el valor de la posicion 1
> L1 = [2, 3 , 4]
> print(L1)
> #Salida: [2, 3, 4]
>
> del L1[1] #-> Aqui le pasamos la posicion del valor
> print(L1)
> #Salida: [2, 4]
> ```

> [!NOTE] 
> ## Eliminar ultimo elemento de una lista
> - Para eliminar el ultimo elemento de una lista, usamos el método '.pop()'
>
> ```python
> # Quiero remover el ultimo elemento de la lista
> L1 = [2, 3 , 4]
> print(L1)
> #Salida: [2, 3, 4]
>
> L1.pop()
> print(L1)
> #Salida: [2, 3]
> ```

> [!NOTE] 
> ## Longitud de una lista
> - Para conocer la longitud de una lista, usamos el método 'len('nombre de la lista')'
>
> ```python
> # Quiero conocer la longitud de L1
> L1 = [2, 3 , 4]
> print(L1)
> #Salida: [2, 3, 4]
>
> print(len(L1))
> #Salida: 3
> ```

> [!NOTE] 
> ## Imprimir los elementos de una lista
> - Para imprimir los elementos de una lista usamos un bucle 'for'
> ```python
> # Quiero imprimir los elementos de L1
> L1 = [2, 3 , 4]
> for i in L1:
>     print(i)    
> #Salida:
> # 2
> # 3
> # 4
> ```

> [!NOTE] 
> ## Transformar una cadena de caracteres a lista
> - Para transformar una cadena de caracteres en una lista, usamos el método 'list()'
> ```python
> # Quiero transformar la cadena de caracteres de la variable palabra
> palabra = "David"
> conversion = list(palabra)    
> print(conversion)
> #Salida: ['D', 'a', 'v', 'i', 'd']
> ```
