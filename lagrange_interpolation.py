from math import *

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

datosf = [(0.0, -3.0), (1.0, 0.0), (3.0, 5.0), (6.0, 7.0)]
Pf = LagrangePol(datosf)
print("\n" + r"Polinomio de Lagrange en x=1.8: " + "\n")
print(Pf(1.8))