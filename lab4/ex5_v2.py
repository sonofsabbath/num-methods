import numpy as np


def f(x):
    return np.cos(x[0] + x[1]) * np.sin(x[0] - x[1])


def derivative(x):
    df = np.zeros(2)
    df[0] = np.cos(x[0] - x[1]) * np.cos(x[0] + x[1]) - np.sin(x[0] - x[1]) * np.sin(x[0] + x[1])
    df[1] = - np.sin(x[0] - x[1]) * np.sin(x[0] + x[1]) - np.cos(x[0] - x[1]) * np.cos(x[0] + x[1])
    return df


def gradient_descent(x, alpha, eta, epochs):
    f_val = f(x)
    f_prev = f_val * 10000
    e = 0

    while e < epochs and np.abs(f_prev - f_val) >= eta:
        f_prev = f_val
        grad = derivative(x)
        x[0] -= alpha * grad[0]
        x[1] -= alpha * grad[1]

        f_val = f(x)
        e += 1

    return x, f_val


def global_optimum(tries, alpha, eta, epochs):
    x12 = []
    vals = []

    for i in range(tries):
        x_init = np.random.randn(2)
        xx, nval = gradient_descent(x_init, alpha, eta, epochs)
        x12.append(xx)
        vals.append(nval)
        print('Attempt {}:\nx1: {}, x2: {}, value = {}'.format(i+1, xx[0], xx[1], nval))

    imin = int(np.argmin(vals))
    print('\nGlobal minimum is {}, found at {}'.format(vals[imin], x12[imin]))


attempts = 1000
l_rate = 0.01
prec = 0.00001
max_epochs = 10000
global_optimum(attempts, l_rate, prec, max_epochs)
