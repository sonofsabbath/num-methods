from numpy import pi


class Figure:
    """Stores names of figures, numbers of parameters the fields' formulas takes and formulas themselves"""

    def __init__(self, n, pars, form):
        self.name = n
        self.parameters = pars
        self.formula = form
        mapping[self.name] = self


def count_fields(fig):
    field = -1
    try:
        if fig == [] or (len(fig) - 1) != fig[0].parameters:
            print('Entered too many or not enough parameters')
        else:
            try:
                field = fig[0].formula(fig[1:])
            except TypeError:
                print('Parameters must be numbers')
    except AttributeError:
        print('Enter name of figure first')

    return field


mapping = {}
circle = Figure('circle', 1, lambda x: pi * x[0] ** 2)
rectangle = Figure('rectangle', 2, lambda x: x[0] * x[0])
triangle = Figure('triangle', 2, lambda x: (x[0] * x[1]) / 2)
rhombus = Figure('rhombus', 2, lambda x: (x[0] + x[1]) / 2)

try:
    f_name = 'triangle'.lower()
    f = mapping[f_name]
    print(count_fields([f, 3, 5]))
except NameError:
    print('Unrecognized figure')
