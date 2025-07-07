import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x)
def f(x):
    return 1 - (x - 2)**2

# Crear valores de x y calcular valores de f(x)
x = np.linspace(-1, 5, 500)  # Rango de valores de x
y = f(x)

# Graficar la función
plt.plot(x, y, label='f(x) = 1 - (x - 2)^2', color='blue')

# Agregar detalles a la gráfica
plt.title("Gráfica de la función f(x) = 1 - (x - 2)^2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Eje X
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Eje Y
plt.legend()
plt.grid()

# Mostrar la gráfica
plt.show()
