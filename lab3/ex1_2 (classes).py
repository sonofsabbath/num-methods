import numpy as np


class Figure:
    """Stores names of figures, numbers of parameters the fields' formulas takes and formulas themselves"""

    def __init__(self, n, pars, form):
        self.name = n
        self.parameters = pars
        self.formula = form
        mapping[self.name] = self


def count_fields(fig):
    field = -1
    if (len(fig) - 1) != fig[0].parameters:
        print('Entered too many or not enough parameters')
    else:
        try:
            if sum(n <= 0 for n in fig[1:]) == 0:
                field = fig[0].formula(fig[1:])
            else:
                print('Parameters must be higher than 0')
        except TypeError:
            print('Parameters must be numbers')

    return field


def compare_fields(figs):
    if not figs:
        print('At least one figure is needed')
        return -1

    fields = []
    for i in figs:
        print(i)
        try:
            f_name = i[0].lower()
            i[0] = mapping[f_name]

            f = count_fields(i)
            fields.append(f)
            if f != -1:
                print(f)
        except KeyError:
            print('Unrecognized figure')
            fields.append(-1)
        except AttributeError:
            print('Enter name of figure first')
            fields.append(-1)
        except IndexError:
            print('Entered empty figure data')
            fields.append(-1)

    f_max = max(fields)
    max_figs = []
    for i in range(len(fields)):
        if fields[i] == f_max and fields[i] != -1:
            max_figs.append((figs[i][0].name, i))

    print('Max field:', str(f_max), '\nFigure(s) and index(es):', max_figs)


mapping = {}
circle = Figure('circle', 1, lambda x: np.pi * x[0] ** 2)
rectangle = Figure('rectangle', 2, lambda x: x[0] * x[0])
triangle = Figure('triangle', 2, lambda x: (x[0] * x[1]) / 2)
rhombus = Figure('rhombus', 2, lambda x: (x[0] + x[1]) / 2)

compare_fields([['rhombus', 9, 2.4], ['circle', 2.5], ['circle', 2.5], ['triangle', 'xd', 4]])
