import numpy as np

# Generar una matriz de 1000x1000 con valores aleatorios entre 1 y 1,000,000
matrix_size = 1000
file_path = 'matrix.txt'
np.random.seed(0)  # Fijar la semilla para reproducibilidad
random_matrix = np.random.randint(1, 1000001, size=(matrix_size, matrix_size))

with open(file_path, 'w') as file:
    for row in random_matrix:
        file.write(' '.join(map(str, row)) + '\n')

print(f'Matriz de {matrix_size}x{matrix_size} generada con valores aleatorios en {file_path}')
