#!/usr/bin/env python
from math import sin, cos
from types import LambdaType

def diff(x0: float, f: LambdaType, n:int = 1_000, delta: float = 0.01)->list[float]:
    x =  [x0 + delta * i for i in range(n+1)]
    fx = [f(elem) for elem in x]
    return [(fx[i+1]- fx[i])/(delta) for i in range(n)]

def calc_error(truth: list[float], approx: list[float]) -> list[float]:
    return [abs(t - a) for t, a in zip(truth, approx)]

def main():
    x0:    float  = 0.0
    delta: float  = 0.01
    n:     int    = 10

    f: LambdaType = lambda x : sin(x)
    df:LambdaType = lambda x : cos(x)
    
    #   [x1, x2, ..., xn]
    x = [x0 + delta * i for i in range(1,n+1)]

    approx:list[float] = diff(x0, f, n=n, delta=delta)
    truth: list[float] = [df(elem) for elem in x]
    error: list[float] = calc_error(truth, approx)

    print(f"{approx=}")
    print(f"{truth=}")
    print(f"{error=}")

if __name__ == "__main__":
    main()

