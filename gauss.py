import numpy as np

def gauss(matriz):
    
    # Obtener el número de filas y columnas
    filas, columnas = matriz.shape

    print("Matriz aumentada inicial:")
    print(matriz)

    # Eliminación gaussiana descendente
    for i in range(filas):
        # Pivote actual
        pivote = matriz[i, i]

        # Hacer el pivote igual a 1
        matriz[i, :] /= pivote

        print(f"\nHaciendo el elemento ({i+1},{i+1}) igual a 1:")
        print(matriz)

        # Hacer ceros por debajo del pivote
        for j in range(i + 1, filas):
            factor = matriz[j, i]
            matriz[j, :] -= factor * matriz[i, :]

            print(f"\nRestando {factor} la fila {i+1} de la fila {j+1}:")
            print(matriz)

    # Eliminación gaussiana ascendente
    for i in range(filas - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            factor = matriz[j, i]
            matriz[j, :] -= factor * matriz[i, :]

            print(f"\nRestando {factor} la fila {i+1} de la fila {j+1}:")
            print(matriz)

    return matriz

# Ejemplo de uso
matriz = np.array([[2.0, 1.0, -1.0, 8.0],
                    [-3.0, -1.0, 2.0, -11.0],
                    [-2.0, 1.0, 2.0, -3.0]])

resultado = gauss(matriz.copy())
print("\nMatriz Escalonada Reducida:")
print(resultado)
print("\nSoluciones: ")
print("x = ", resultado[0,3])
print("y = ", resultado[1,3])
print("z = ", resultado[2,3])
