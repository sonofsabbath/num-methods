import numpy as np
from scipy.optimize import fmin


def f(x):
    return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0] ** 2)) + 0.01 * np.abs(x[0] + 10)  # Bukin function No. 6


def gradient_descent(x, alpha, eta, epochs):
    e = 0
    f_prev = 100
    f_val = 0
    df = np.zeros(2)

    while e < epochs and np.abs(f_prev - f_val) >= eta:
        f_prev = f_val
        df[0] = (0.01 * (x[0] + 10)) / np.abs(x[0] + 10) - (x[0] * (x[1] - 0.01 * x[0] ** 2)) / (np.abs(x[1] - 0.01 * x[0] ** 2)) ** (3 / 2)
        df[1] = (50 * (x[1] - 0.01 * x[0] ** 2)) / np.abs(x[1] - 0.01 * x[0] ** 2) ** (3 / 2)
        x[0] -= alpha * df[0]
        x[1] -= alpha * df[1]

        f_val = f(x)
        e += 1

    return x, f_val


def global_optimum():
    xs = []
    vals = []
    failures = 0
    trials = 0

    for i in range(-11, 3):
        for j in range(-1, 2):
            x12, value = gradient_descent([i, j], 0.0001, 0.0001, 25000)
            if not np.isnan(value):
                xs.append(x12)
                vals.append(value)
            else:
                failures += 1
            trials += 1

            x12 = [i, j]
            value = f(x12)
            if not np.isnan(value):
                xs.append(x12)
                vals.append(value)
            else:
                failures += 1
            trials += 1

    ind = int(np.argmin(vals))
    rate = "{:.2f}%".format(((trials - failures) / trials) * 100)
    return xs[ind], vals[ind], rate


res, val, rating = global_optimum()
print('trying to find global minimum using my function')
print('learning rate: 0.0001, precision: 0.0001, max_epochs: 25000')
print('global optimum at', res, ', optimal value:', val)
print('success / total trials rate (for local optimas):', rating, '\n')

print('trying to find global minimum using scipy')
x0 = np.random.randn(2)
scimin = fmin(f, x0)
scival = f(scimin)

print('\ndifference between my function and scipy:', np.abs(val - scival))
if val < scival:
    print('my function found lower value')
else:
    print('scipy found lower value')
