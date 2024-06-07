import random
import time

# Pedir al usuario la cantidad de números a organizar
cantidad_numeros = int(input("Ingrese la cantidad de números a organizar: "))

# Generar la lista de números aleatorios
numeros = [random.randint(1, 1000) for _ in range(cantidad_numeros)]

print("Lista de números generados:", numeros)

# Registrar el tiempo de inicio
tiempo_inicio = time.time()

# Implementar el algoritmo de ordenamiento de burbuja con for
for _ in range(len(numeros)):
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i + 1]:
            numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]

# Registrar el tiempo de finalización
tiempo_fin = time.time()

# Calcular el tiempo de ejecución
tiempo_ejecucion = tiempo_fin - tiempo_inicio

print("Lista de números ordenados:", numeros)
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
