import numpy as np  # Importamos la librería NumPy para trabajar con matrices

def contarPuntosCalientes(matriz):
    filas, columnas = matriz.shape  # Obtenemos el tamaño de la matriz
    contador = 0  # Inicializamos el contador

    # Recorremos solo las celdas que NO están en el borde
    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):
            valor = matriz[i, j]  # Valor de la celda actual

            # Obtenemos los 8 vecinos manualmente
            vecinos = [
                matriz[i-1, j-1], matriz[i-1, j], matriz[i-1, j+1],
                matriz[i, j-1],                 matriz[i, j+1],
                matriz[i+1, j-1], matriz[i+1, j], matriz[i+1, j+1]
            ]

            promedio = sum(vecinos) / 8  # Calculamos el promedio

            if valor >= 5 * promedio:  # Condición de punto caliente
                contador += 1

    return contador # Retornamos el contador de puntos calientes

def detectarPuntosCalientes(matriz):
    filas, columnas = matriz.shape
    posiciones = []  # Lista vacía para guardar coordenadas

    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):
            valor = matriz[i, j]

            vecinos = [
                matriz[i-1, j-1], matriz[i-1, j], matriz[i-1, j+1],
                matriz[i, j-1],                 matriz[i, j+1],
                matriz[i+1, j-1], matriz[i+1, j], matriz[i+1, j+1]
            ]

            promedio = sum(vecinos) / 8

            if valor >= 5 * promedio:
                posiciones.append((i, j))  # Guardamos la posición

    return posiciones

def etiquetarMapa(matriz, posiciones):
    for i, j in posiciones:
        matriz[i, j] = 999  # Reemplazamos el valor por 999
    return matriz # Retornamos la matriz modificada


# Creamos una matriz de ejemplo
matriz = np.array([
    [1, 2, 1, 2],
    [2, 100, 2, 1],
    [1, 2, 1, 2],
    [2, 1, 2, 1]
])

# Contamos puntos calientes
cantidad = contarPuntosCalientes(matriz) #Activamos la función contarPuntosCalientes
print("Cantidad de puntos calientes:", cantidad)

# Detectamos coordenadas
posiciones = detectarPuntosCalientes(matriz) # Activamos la función detectarPuntosCalientes
print("Posiciones de puntos calientes:", posiciones)

# Etiquetamos en una copia de la matriz
matriz_etiquetada = etiquetarMapa(matriz.copy(), posiciones) # Activamos la función etiquetarMapa

# Imprimimos la matriz final
print("Matriz final:")
print(matriz_etiquetada)
