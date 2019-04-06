from numpy import pi


class Figure:
    """Stores names of figures and formulas for their field"""

    def __init__(self, form):
        self.formula = form


circle = Figure(lambda x: pi * x ** 2)
rectangle = Figure(lambda x, y: x * y)
triangle = Figure(lambda x, y: (x * y) / 2)
rhombus = Figure(lambda x, y: (x + y) / 2)
