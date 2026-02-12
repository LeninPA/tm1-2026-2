#!/usr/bin/env python
"""
Script para hacer regresión lineal simple
"""

def rls(x: list[float], y: list) -> list[float]:
    n = len(x)
    
    xy = [xi * yi for xi, yi in zip(x, y)]
    x2 = [xi ** 2 for xi in x]

    suma_x = sum(x)
    avg_x = suma_x / n
    suma_y = sum(y)
    avg_y = suma_y / n
    suma_xy = sum(xy)
    suma_x2 = sum(x2)

    alfa = (suma_xy - avg_y * suma_x)/(suma_x2 - avg_x * suma_x)
    beta = avg_y - alfa * avg_x

    return [alfa, beta]

def main():
    x = [63, 52, 50, 55, 57, 60, 63, 51] # Temp en Farenheit
    y = [80, 45, 37, 67, 58, 79, 89, 46] # Chirridos grillo
    print(rls(x, y))

if __name__ == "__main__":
    main()
