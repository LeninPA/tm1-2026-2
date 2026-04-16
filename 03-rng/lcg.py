from random import random

def lcg(x_n: int, a: int, c: int, m:int)->int:
    return (a * x_n + c) % m

def normalize(l: list):
    m = max(l)
    return [elem / m for elem in l]

def main():
    print("Número aleatorio:")
    print(random())
    params = [
        (8,5,3,0),
        (8,4,1,0),
        (16, 1, 0, 12),
        (16, 5, 0, 1),
    ]
    n = 50
    for m, a, c, x_0 in params:
        steps = [lcg(x_0, a, c, m)]
        for _ in range(n):
            steps.append(lcg(steps[-1], a, c, m))
        print(f"{m=} -- {a=} -- {c=} -- {x_0=} -- ")
        print(normalize(steps))
        print("-"*10)

if __name__ == "__main__":
    main()
