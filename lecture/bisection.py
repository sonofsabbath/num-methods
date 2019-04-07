from numpy import abs


def bisection(a, b, eps):
    if f(a) * f(b) >= 0:
        print('Incorrect a, b')
    while abs(b - a) >= eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(c)


def bisect_fix(a, b, eps, sig):
    if sign(f(a)) == sign(f(b)):  # uniknięcie niedomiaru/nadmiaru ze zbędnego mnożenia
        print('Incorrect a, b')
    c = (a + b) / 2
    while abs(b - a) >= eps or f(c) > sig:  # kończymy gdy błąd jest dostacznie mały i f(c) jest bardzo bliskie zeru
        c = a + (b - a) / 2   # lepiej dodać coś do poprzedniej wielkości; może się zdarzyć, że c wyjdzie poza [a,b]
        if f(c) == 0:
            return c
        elif sign(f(a)) != sign(f(c)):
            b = c
        else:
            a = c
    print(c)


def f(x):
    return x ** 3 - x ** 2 + 2


def sign(x):
    if x >= 0:
        return 1
    else:
        return 0


bisection(-200, 100, 0.0001)
bisect_fix(-200, 100, 0.0001, 0.00000000001)
