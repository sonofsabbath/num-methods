import numpy as np


def f(x):
    return np.cos(x[0] + x[1]) * np.sin(x[0] - x[1])


def derivative(x):
    df = np.zeros(2)
    df[0] = np.cos(x[0] - x[1]) * np.cos(x[0] + x[1]) - np.sin(x[0] - x[1]) * np.sin(x[0] + x[1])
    df[1] = - np.sin(x[0] - x[1]) * np.sin(x[0] + x[1]) - np.cos(x[0] - x[1]) * np.cos(x[0] + x[1])
    return df


def gradient_descent(x, alpha, eta, epochs):
    f_prev = 100
    f_val = 0
    e = 0

    while e < epochs and np.abs(f_prev - f_val) >= eta:
        f_prev = f_val
        grad = derivative(x)
        x[0] -= alpha * grad[0]
        x[1] -= alpha * grad[1]

        f_val = f(x)
        e += 1

    return x, f_val

