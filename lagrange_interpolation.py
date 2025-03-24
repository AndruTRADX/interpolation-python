from math import *
import numpy as np
import matplotlib.pyplot as plt

def LagrangePol(datos):
    def L(k, x):
        out = 1.0
        for i, p in enumerate(datos):
            if i != k:
                out *= (x - p[0]) / (datos[k][0] - p[0])
        return out

    def P(x):
        lag = 0.0
        for k, p in enumerate(datos):
            lag += p[1] * L(k, x)
        return lag

    return P

# Datos proporcionados
datosf = [
    (3.0, 118.305),
    (6.0, 203.22),
    (9.0, 254.745),
    (12.0, 272.88),
    (15.0, 257.625),
    (18.0, 209.1562)
]

# a) Construir el polinomio de interpolación
Pf = LagrangePol(datosf)
print(Pf)

# b) Reconstruir datos desde t=0 hasta t=24
datos_reconstruidos = [(t, Pf(t)) for t in range(25)]

# Mostrar tabla de datos reconstruidos
print("Tabla de datos reconstruidos:")
print("t  | Valor")
print("---|-------")
for t, valor in datos_reconstruidos:
    print(f"{t:2} | {valor:.4f}")

# c) Graficar
x_vals = np.linspace(0, 24, 1000)
y_vals = [Pf(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Polinomio de Interpolación', color='blue')
plt.scatter(
    [p[0] for p in datosf],
    [p[1] for p in datosf],
    color='red',
    label='Datos Originales',
    zorder=5
)
plt.scatter(
    [p[0] for p in datos_reconstruidos],
    [p[1] for p in datos_reconstruidos],
    color='green',
    marker='x',
    s=100,
    label='Datos Reconstruidos',
    zorder=4
)
plt.legend()
plt.xlabel('t (segundos)')
plt.ylabel('Valor')
plt.title('Interpolación de Lagrange y Datos')
plt.grid(True)
plt.show()