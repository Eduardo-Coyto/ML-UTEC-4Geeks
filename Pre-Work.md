---


## ¿Qué es una lista?

Un lista es, normalmente, cualquier colección de valores. Las reglas de cómo agregar o eliminar elementos de esa lista pueden cambiar de un lenguaje de programación a otro. Pero - en general - son las únicas formas en que los desarrolladores pueden crear elementos.
Las listas no son la única forma en que tenemos que enumerar las cosas almacenar múltiples valores de una sola vez pero es la más usada para ese propósito. Por ejemplo: lista de estudiantes, lista de artistas, lista de transacciones ... ¡cualquier cosa!

Este tipo de datos hace muchas más cosas que los otros. Las listas son la única forma de almacenar más de un tipo de datos en la misma variable.

Cada lista tiene los mismos conceptos básicos:

**The items:** Son los valores reales dentro de cada posición de la lista.

**The length:** es el tamaño de la lista (cuántos items tiene la lista).

**Index:** es la posición del elemento.

![image](https://user-images.githubusercontent.com/79756539/167164260-97676799-863c-419a-99e9-63c28a105ab4.png)


![¿qué es una lista?](../../assets/images/7ed2c414-0d00-4e68-b659-b65c26d1983a.png)

> :point_up: Las posiciones de la comienzan con **cero (0)**; el primer elemento es el elemento en la posición **cero (0)**

## ¿Como Declarar una Lista?


Utilizando corchetes de la siguiente manera:

```python
myList = [] #lista vacia
myList = ["Apple", "Orange", "Donkey"] # La única forma de declarar una lista
myTuple = ("Apple", "Orange", "Donkey") # Esto no es una lista, es una version más limitada llamada "Tupla"
mySet = {"Apple", "Orange", "Donkey"} # Esto no es una lista, es una version más limitada llamada "set" (cojunto).
```

## Acceder a los items en la lista 

Para acceder a un elemento específico en una lista, necesita un `index` o índice. Un índice es un valor entero que representa la posición del arreglo a la que desea acceder/obtener/recuperar.

El índice siempre debe comenzar en cero (0). Eso significa que una lista de 2 elementos puede tener un índice = 0 o un índice = 1. Tratar de obtener la segunda posición devolverá "indefinido" porque significará que estamos tratando de acceder al tercer elemento (que no existe). Por ejemplo, para obtener cualquier elemento de la lista puede hacer lo siguiente:

```python
    print(myList[0])  # Esto imprimirá el 1er elemento en la consola.
    aux = myList[5]
    print(aux); # Esto imprimirá el 4to elemento en la consola.
    print(myList[myList.length-1]);  #vEsto imprimirá el último elemento en la consola.
```

## Actualizar Elementos en el Arreglo

Si lo deseas, puedes restablecer o actualizar cualquier elemento dentro de un arreglo usando el índice como este:

```python
    myList[5] = 'Whatever value'
    # Esto asignará el valor 'Whatever value' en el sexto elemento de la lista.
```

## Añadiendo elementos a una lista (función append o insert)

Hay dos formas de agregar un nuevo elemento: final de la lista o donde tu quieras, y necesitemos usar las funciónes append e insert respectivamente para eso.

### Utilizando `append` en las listas de Python

```python
    myList = ['Pedro','Juan','Maria']
    myList.append('Chris') # esto agrega a chris al final del arreglo
    print(myList); # esto imprimirá ['Pedro','Juan','Maria','Chris'];
```

### Utilizando `insert` (seleccionando posición) en Python

La ventaja de utilizar insert es que te permite seleccionar la posicion donde deseas insertar el elemento en el array:

```python
    myList = ['Pedro','Juan','Maria']
    myList.insert(1,'Chris') # esto agrega a chris entre Pedro y Juan
    print(myList); # esto imprimirá ['Pedro','Chris','Juan','Maria'];
```

> :point_up: La funcion `insert` es mucho mas lenta que `append`, deberias tratar de eviarla.

## Eliminando items de una lista con Python(función pop, remove, delete)

A diferencia de otros lenguajes como Javascript, Python cuenta con varias funciones para remover elementos de un array: Pop, Remove, Delete.

### Eliminando elementos de una lista con POP

Eliminar un elemento utilizando `pop` tiene exactamente las mismas limitaciones que al agregar un elemento utilizando `append`: solo permite eliminar un elemento de la última posición de la lista. 

```python
    myList = ['Pedro','Chris','Juan','Maria']
    myList.pop()
    print(myList) # esto imprimirá ['Pedro','Chris','Juan']
```

### Eliminando elementos de una lista con Remove

Te permitirá eliminar la primera ocurrencia de un elemento por su nombre.

```python
    #Si deseas eliminar 'Chris', necesitas hacer lo siguiente: 
    myList = ['Pedro','Chris','Juan','Maria']
    myNewArray.remove(2)
    print(myList) # esto imprimirá ['Pedro','Chris','Juan'];
```

### Eliminando elementos de una lista con Delete

Una de las funcionalidades mas útiles de `del` es que puedes eliminar muchos elementos de una sola vez. Debes especificar la posición de partida y de término.

```python
    #Si deseas eliminar 'Chris', necesitas hacer lo siguiente: 
    myList = ['Pedro','Chris','Juan','Maria','Pepe','Mario','Bob']
    del myList[2:5]
    print(myList) # esto imprimirá ['Pedro', 'Chris', 'Mario', 'Bob']
```

## Iterando sobre una lista (bucles)


Normalmente, cuando trabajes con listas, tendrás que recorrer todos los items. Por ejemplo: ordenándolos manualmente; cambiar su orden, filtrarlos, etc.

Hay varias formas de recorrer una lista, pero la mas utilizada es la funcion `for`:

```python
myList = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]
for number in myList:
    print(number)
```

## Iterando usando la posicion

A veces es útil recorrer un arreglo utilizando la posicion:

```python
for i in range(0,len(myList)):
    print("La posicion es "+str(i)+" para el elemento "+myList[i])

### Imprimira lo siquiente
# La posicion es 0 para el elemento Pedro
# La posicion es 1 para el elemento Chris
# La posicion es 2 para el elemento Mario
# La posicion es 3 para el elemento Bob
```

## ¿Qué son las Funciones?

Básicamente, una función un conjunto de lineas de código agrupadas para cumplir un objectivo específico, por ejemplo veamos esta función para multiplicar dos números:

```python
def multiplicar(a,b):
    return a*b

resultado = multiplicar(2,6)
print(str(resultado)) # imprime 12
```

Analizando el código de arriba tenemos las siguientes conclusiones:

- Para crear una función debemos utilizar la sentencia `def`.
- Luego de `def` colocamos el nombre que le queremos dar a la función (en este caso "multiplicar").
- Después del nombre debemos colocar entre paréntesis los parámetros o entradas que tendrá la función separados por coma (en este caso `a` y `b`). Puedes escoger el nombre de los   parámetros pero siempre deben tener el mismo orden.
- Tenemos que terminar la linea con dos puntos `:`, de esa forma el computador sabrá que vamos a empezar a programar una función (algoritmo).
- Por ultimo debemos añadir un `return`(es una buena práctica), toda función debe retornar algo, asi sea `None`, en este caso retornamos la multiplicación entre los parámetros A y B (entradas).

De ahora en adelante cada vez que quiera multiplicar dos numeros puedo re-utilizar la función `multiplicar` de la siguiente manera, cuantas veces lo necesites:

```python
resultado1 = multiplicar(2,6)
print(str(resultado1)) # imprime 12

resultado2 = multiplicar(5,2)
print(str(resultado1)) # imprime 10
```

> :tv: Haz clic aquí para ver un [video explicativo sobre funciones](https://www.youtube.com/watch?v=_C7Uj7O5o_Q) (10min)

### Segundo ejemplo sobre funciones

Veámos esta función que dado un numero de invitados permite calcular el costo de organizar una fiesta con el siguiente algoritmo:

1. Primero se debe conocer el numero de invitados (se le debe pasar como parámetro a la función)
2. El costo general de una fiesta es de 10 dolares por invitados
3. Si hay mas de 200 invitados se ofrece un descuento de 10%.

```python
def calcular_costo(numero_de_invitados):
    precio_por_invitado = 10
    costo_total = numbero_de_invitados * precio_por_invitado
    if numero_de_invitados > 200:
        costo_total = costo_total - (costo_total * 0.1) # ← descuento de 10%
    return costo_total

```
<iframe height="400px" width="100%" src="https://repl.it/@4GeeksAcademy/calcular-costo-fiesta?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

### Datos importantes sobre las funciones en Python:

1. **Cada función debe tener un propósito.** (un objetivo) (como nuestra función "multiplicar"). El propósito de la función es calcular la multiplicación entre dos números dados.
2. **Debe tener un nombre único.**  En este caso particular, nuestra función se llama "multiplicar", que es un gran nombre porque sabes exactamente qué hace la función, es explícita.
3. **Debe devolver algo**  De forma predeterminada, en Python, todas las funciones devuelven `None`, pero debes reemplazarlo y siempre devolver algo útil. En este ejemplo, queremos devolver el resultado de una multiplicación de a & b.
4. **Las funciones pueden tener parámetros.**  Un "parámetro" es una variable que la función puede recibir al principio de su código (como a y b en nuestro ejemplo).

La idea es tener una librería de cientos de funciones y usarlas como nos plazca, declaras todas tus funciones y luego empiezas a usarlas y reutilizarlas todo el tiempo.

## Pero, ¿Por qué usar Funciones en lugar de simplemente hacer todo en una gran porción de código?

La codificación es muy abstracta y sucede mucho que no tienes idea de lo que escribiste ayer. Antes de que existieran las funciones, los algoritmos eran una enorme serie interminable de líneas de código donde los desarrolladores tenían dificultades y se perdían. Es difícil para tu cerebro seguir un procedimiento / algoritmo de gran longitud; Cuantas más líneas de código, más abstracto se vuelve.

Al utilizar funciones tienes las siguientes ventajas:

1. **Dividir y conquistar**: divide tu algoritmo en sub-algoritmos más pequeños y concéntrate en un problema a la vez.
2. **Menos código**: Mientras menos codigo mejor, cuando usas funciones estas pensando en reutilizar en lugar de copiar y pegar.
3. **Reutiliza tu código** llamando a la función varias veces, reduciendo drásticamente la longitud de tu código.
4. **Organiza tu código**: los nombres de las funciones te dirán qué hace esa parte del código, puedes tener todas las funciones en un archivo separado y reutilizarlas en todos sus desarrollos futuros.

> :point_up: Si lo piensas bien, las funciones son equivalentes a los libros. Almacenan funciones y formas de hacer las cosas y en futuros desarrollos simplemente los reutilizas en lugar de tener que resolver todo de nuevo.

## El Alcance de la Función

Todas las funciones deben comenzar y terminar en algún lugar, esto se llama **alcance de la función**. Puedes delimitar los límites de la función utilizando identación de la siguiente manera:

```python

# esta parte del código está FUERA de la función 'multiplicar'

def multiplicar(a, b):

    # esta parte del código está DENTRO de mi función 
    # porque esta despues de la declaración e identada a la derecha
    
    return a * b;

    # esta parte del código está DENTRO
    # pero nunca se ejecutará porque se encuentra DESPUÉS de del return


# esta parte del código está FUERA de la función 'multiplicar' 
# porque ya no tiene la identación a la derecha
print(str(multiplica(34, 2)))
```

Cualquier variable que declare dentro de la función no estará disponible fuera de ella.

```python
def multiplicar(a, b):
   miVariable = 'hello'
   return a * b

# este print no funcionará, generará un error, porque myVariable fue 
# declarado dentro de la función multiplicar, por lo tanto no está disponible fuera de su alcance.
print(myVariable)
```

> :point_up:  Es muy importante recordar que una vez que use la instrucción `return`, la función dejará de ejecutarse, si hay algún código después de esa instrucción, nunca se ejecutará.


```python
def multiplicar(a, b):
   miVariable = 'hello'
   return a * b

# este print no funcionará (generárá un erroe) porque miVariable se declaró dentro de la función multiplicar
# por lo que no está disponible fuera de la función
print(miVariable)
```

## Funciones Lambda (funciones de una línea)

Si tu función va a tener una sola linea de código puedes declararla de una forma mucho mas ágil utilizando la parabra reservada `lambda`.

```python
multiplicar = lambda a, b : a * b
resultado = multiplicar(2,3)
print(str(resultado))
```

Lamba es ideal para casos en los que tengas funciones muy pequeñas. Aprenderás a quererlas por lo rápido que resulta codificar, especialmente cuando tengas que iterar arrays.

## Llamando funciones

La única forma de usar una función (es decir de "llamarla") es usando paréntesis de esta forma:

```python
# Así se llama a una función sin parámetros  
multiplicar()

# Así se llama a una función con parámetros
multiplcar(<primer param>,<segundo param>)

# por ejemplo, para multiplicar 3 
multiplar(3,9)
```

Recuerda asignarle a la función cel parámetro que debiese recibir. En nuestro ejemplo, la función multiplicar se declaró pidiendo dos números para multiplicar. J

## Llamando funciones de forma anidada

Puedes combinar funciones como quieras y tener llamadas encadenadas como esta:

```python
def suma(a,b):
   return a+b

def multiplicar(a,b)
   return a*b

resultado = multiplicar(suma(3,5),suma(1,1)))


# Las ejecuciones van de adentro hacia afuera. 
# Primero, se calculará la suma de 3 + 5 y 1 + 1. 
# A continuación, se multiplicarán sus respectivos resultados. 
primero = suma(3,5)
segundo = suma(1,1)
print(str(multiplicar(primero, segundo))
```

> :point_up: [Ve este ejemplo en vivo en replit](https://repl.it/@4GeeksAcademy/nested-function-calling-python)

## Veamos un ejemplo:

El siguiente código tiene 3 funciones declaradas:

```python
def get_average(ages):
    # algo de código

def get_youngest(ages):
    # algo de código

def get_person_info(name):
    # algo de código
```

Como puedes ver, los nombres de las funciones son bastante específicos sobre lo que hacen las funciones, así como los parámetros asignados a ellas.

<iframe height="400px" width="100%" src="https://repl.it/@4GeeksAcademy/functions-example-python?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Otras cosas importantes a tener en cuenta:

+ Estamos llamando a la función `get_person_info` dos veces, sin usar funciones tendríamos que usar más código porque no tendríamos ninguna opción para reutilizar la función.
+ La función `get_average` es obtener el valor promedio en un array dado. No sabe nada más ¡Y eso es genial! Al separar tu código en pequeñas funciones, puedes concentrarte en una cosa a la vez.
