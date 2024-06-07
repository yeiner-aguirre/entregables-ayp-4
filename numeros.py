import random
import time

# Pedir al usuario la cantidad de números a organizar
cantidad_numeros = int(input("Ingrese la cantidad de números a organizar: "))

# Generar la lista de números aleatorios
numeros = [random.randint(1, 1000) for _ in range(cantidad_numeros)]

print("Lista de números generados:", numeros)

# Registrar el tiempo de inicio
tiempo_inicio = time.time()

# Implementar el algoritmo de ordenamiento de burbuja con while
n = len(numeros)
while n > 1:
    swapped = False
    i = 0
    while i < n - 1:
        if numeros[i] > numeros[i + 1]:
            numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
            swapped = True
        i += 1
    if not swapped:
        break
    n -= 1

# Registrar el tiempo de finalización
tiempo_fin = time.time()

# Calcular el tiempo de ejecución
tiempo_ejecucion = tiempo_fin - tiempo_inicio

print("Lista de números ordenados:", numeros)
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

#escribir un algoritmo que lea una matriz desde un archivo de enteros minimo de 1000x1000, dado un numero por el usuario 
#lo debe de encontrar en la matriz 
#                                          PRUEBAS 
#que el numero este en la primera pocision 
#que el numero este en la mitad
#que el numero este al final
#el numero tiene una probabilidad del 60% de no estar en la matriz
#CALCULAR EL ORDEN DE MAGNITUD PARA LOS 4 PASOS 
#MOSTRAR EL TIEMPO QUE SE DEMORAN LOS 4 CASOS
