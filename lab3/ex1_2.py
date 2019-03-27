from cs50 import *
import numpy as np


def field(fig, x, y=1):
    if x <= 0 or y <= 0:
        print("x and y both must be higher than zero\nCan't calculate the field of " + fig)
        return 0

    if fig == 'circle':
        f = np.pi * x ** 2
    elif fig == 'rectangle':
        f = x * y
    elif fig == 'triangle':
        f = (x * y) / 2
    elif fig == 'rhombus':
        f = (x + y) / 2
    else:
        print("Unrecognized figure\nCan't calculate the field of " + fig)
        return 0

    print("Field of " + fig + ": " + str(f))
    return f


def compare_figures(figs):
    vals = []
    for i in figs:
        if i[0] == 'circle':
            vals.append(field(i[0], i[1]))
        else:
            vals.append(field(i[0], i[1], i[2]))

    if vals[0] == 0 or vals[1] == 0:
        print("Can't compare - couldn't calculate one or both of the fields")
    else:
        if vals[0] > vals[1]:
            print(str(figs[0][0]) + " has larger field")
        elif vals[0] < vals[1]:
            print(str(figs[1][0]) + " has larger field")
        else:
            print("Figures are equal")


figures = []
for i in range(2):
    figure = get_string("figure: ")
    figure = figure.lower()

    a = get_float("x: ")
    if figure != 'circle':
        b = get_float("y: ")
        figures.append([figure, a, b])
    else:
        figures.append([figure, a])

compare_figures(figures)
