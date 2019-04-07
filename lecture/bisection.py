def f(x):
    return x ** 3.0 - x ** 2.0 + 2.0


def bisection(a, b, eps):
    if f(a) * f(b) >= 0.0:
        return 'Incorrect a, b'
    while (b - a) >= eps:
        c = (a + b) / 2.0
        if f(c) == 0.0:
            return c
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
        print(c)
    return c


bisection(-200.0, 100.0, 0.00001)
