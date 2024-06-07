import time
import numpy as np
import psutil
import os

def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = []
        for line in file:
            matrix.append(list(map(int, line.split())))
    return np.array(matrix)

def find_number_in_matrix(matrix, number):
    rows, cols = matrix.shape
    i, j = 0, 0
    while i < rows:
        j = 0
        while j < cols:
            if matrix[i, j] == number:
                return (i, j)
            j += 1
        i += 1
    return None

def run_test(matrix, number):
    process = psutil.Process(os.getpid())
    
    start_time = time.time()
    start_memory = process.memory_info().rss
    
    position = find_number_in_matrix(matrix, number)
    
    end_time = time.time()
    end_memory = process.memory_info().rss
    
    duration = end_time - start_time
    memory_used = end_memory - start_memory
    
    return position, duration, memory_used

def calculate_order_of_magnitude(time_taken, size):
    # Assuming time_taken is proportional to size^2 (for a brute-force search in a 2D matrix)
    order_of_magnitude = time_taken / (size ** 2)
    return order_of_magnitude

# Leer la matriz desde el archivo
file_path = 'matrix.txt'
matrix = read_matrix_from_file(file_path)
matrix_size = matrix.shape[0]

# Solicitar el número a buscar al usuario
number_to_find = int(input("Introduce el número a buscar en la matriz: "))

# Ejecutar la prueba y mostrar resultados
pos, time_taken, memory_used = run_test(matrix, number_to_find)
order_of_magnitude = calculate_order_of_magnitude(time_taken, matrix_size)

if pos is not None:
    print(f"Número a buscar: {number_to_find}, Posición encontrada: {pos}")
else:
    print(f"Número a buscar: {number_to_find}, no encontrado en la matriz.")

print(f"Tiempo tomado: {time_taken:.6f} segundos")
print(f"Memoria usada: {memory_used / (1024 ** 2):.6f} MB")
print(f"Orden de magnitud (tiempo / tamaño^2): {order_of_magnitude:.6e}")
