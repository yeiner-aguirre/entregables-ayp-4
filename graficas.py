import numpy as np
import matplotlib.pyplot as plt

# Generar 120 números aleatorios enteros del 1 al 50
x = np.random.randint(1, 51, 120)

# Crear las diferentes funciones para las gráficas
def lineal(x):
    return x

def logaritmica_base2(x):
    return np.log2(x)

def semilogaritmica(x):
    return np.log(x)

def cuadratica(x):
    return x**2

def exponencial(x):
    return np.exp(x)

def logaritmica_base8(x):
    return np.log(x) / np.log(8)

# Crear un vector de y para cada función
y_lineal = lineal(x)
y_logaritmica_base2 = logaritmica_base2(x)
y_semilogaritmica = semilogaritmica(x)
y_cuadratica = cuadratica(x)
y_exponencial = exponencial(x)
y_logaritmica_base8 = logaritmica_base8(x)

# Crear las gráficas
fig, axs = plt.subplots(3, 2, figsize=(30, 50))  # Ajustar el tamaño de la figura

# Gráfica lineal
axs[0, 0].plot(x, y_lineal, 'bo-')
axs[0, 0].set_title('Gráfica Lineal')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y = x')
axs[0, 0].grid(True)

# Gráfica logarítmica base 2
axs[0, 1].plot(x, y_logaritmica_base2, 'ro-')
axs[0, 1].set_title('Gráfica Logarítmica (base 2)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y = log2(x)')
axs[0, 1].grid(True)

# Gráfica semilogarítmica
axs[1, 0].plot(x, y_semilogaritmica, 'go-')
axs[1, 0].set_title('Gráfica Semilogarítmica')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y = log(x)')
axs[1, 0].grid(True)

# Gráfica cuadrática
axs[1, 1].plot(x, y_cuadratica, 'mo-')
axs[1, 1].set_title('Gráfica Cuadrática')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('y = x^2')
axs[1, 1].grid(True)

# Gráfica exponencial
axs[2, 0].plot(x, y_exponencial, 'co-')
axs[2, 0].set_title('Gráfica Exponencial')
axs[2, 0].set_xlabel('x')
axs[2, 0].set_ylabel('y = exp(x)')
axs[2, 0].grid(True)

# Gráfica logarítmica base 8
axs[2, 1].plot(x, y_logaritmica_base8, 'yo-')
axs[2, 1].set_title('Gráfica Logarítmica (base 8)')
axs[2, 1].set_xlabel('x')
axs[2, 1].set_ylabel('y = log8(x)')
axs[2, 1].grid(True)

# Ajustar el espaciado entre subgráficas y los márgenes
plt.subplots_adjust(hspace=0.4, wspace=0.4, top=0.95, bottom=0.05, left=0.05, right=0.95)

# Mostrar las gráficas
plt.show()


