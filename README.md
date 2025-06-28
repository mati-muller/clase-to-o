# 🐍 Resumen Detallado para Prueba de Python

---

## 1. Función `print()`

### 🧠 ¿Qué hace?

Imprime información en pantalla.

### Sintaxis:

```python
print("Hola mundo")
```

### Imprimir varios valores:

```python
print("Edad:", 20, "años")
```

### Argumentos especiales:

```python
print("2025", "06", "28", sep="-")     # 2025-06-28
print("Hola", end=" "); print("mundo")   # Hola mundo
```

### Formato de cadenas:

```python
nombre = "Ana"
edad = 22
print(f"Hola {nombre}, tienes {edad} años")
print("Hola {}, tienes {} años".format(nombre, edad))
```

---

## 2. Tipos de Variables

### Tipos comunes:

```python
x = 10        # int
y = 3.14      # float
z = "Hola"    # str
b = True      # bool
```

### Conversión entre tipos:

```python
int("5")
float("3.14")
str(123)
```

### Comprobación de tipo:

```python
type(x)
isinstance(x, int)
```

---

## 3. Condicionales

### Estructura:

```python
x = 7
if x > 5:
    print("Mayor a 5")
elif x == 5:
    print("Igual a 5")
else:
    print("Menor a 5")
```

### Operadores:

* Comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
* Lógicos: `and`, `or`, `not`

### Condicional anidado:

```python
if x > 0:
    if x < 10:
        print("Entre 1 y 9")
```

### Operador ternario:

```python
mensaje = "Positivo" if x > 0 else "Negativo"
```

---

## 4. Módulo `math`

```python
import math
math.sqrt(16)
math.pow(2, 3)
math.pi
math.ceil(2.3)
math.floor(2.9)
math.trunc(3.8)
math.sin(math.pi/2)
```

---

## 5. Módulo `random`

```python
import random
random.random()
random.randint(1, 10)
random.uniform(1, 5)
random.choice(["A", "B", "C"])
random.sample(range(10), 3)
random.shuffle(lista)
random.seed(42)
```

---

## 6. Módulo `time`

```python
import time
time.time()
time.sleep(2)
time.ctime()
time.gmtime()
```

---

## 7. Ciclos

### `for` con `range()`:

```python
for i in range(5):
    print(i)
```

* `range(5)` genera: `0, 1, 2, 3, 4`
* Empieza desde 0 hasta **n-1**

### `while`:

```python
x = 0
while x < 3:
    print(x)
    x += 1
```

### Control de flujo:

```python
for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print(i)
```

### `else` en bucles:

```python
for i in range(3):
    print(i)
else:
    print("Fin")
```

---

## 8. Listas

### Creación e indexación:

```python
lista = [1, 2, 3]
print(lista[0])
```

* Primer elemento es `lista[0]`

### Métodos:

```python
lista.append(4)
lista.insert(1, 99)
lista.pop()
lista.remove(99)
lista.sort()
lista.reverse()
```

### Slicing:

```python
print(lista[1:3])
print(lista[::-1])
```

### List comprehension:

```python
cuadrados = [x**2 for x in range(5)]
```

---

## 9. Ciclos Anidados

### Ejemplo:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

### Matriz:

```python
matriz = [[1,2], [3,4]]
for fila in matriz:
    for val in fila:
        print(val)
```

---

## 10. NumPy

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.zeros((2,2))
c = np.ones(3)
d = np.arange(0, 10, 2)

a[0]        # primer elemento
a[1:3]      # slicing

np.sqrt(a)
np.dot(a, a)
```

---

## 11. Funciones `def`

### Definición:

```python
def saludar():
    print("Hola")
```

### Con parámetros:

```python
def saludar(nombre):
    print(f"Hola {nombre}")
```

### Con retorno:

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
```

---
