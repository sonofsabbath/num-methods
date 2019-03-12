import cs50 as cs
import numpy as np

x = cs.get_float("x: ")
y = cs.get_float("y: ")

if x <= 0 or y <= 0:
    print("Radius must be higher than zero")
else:
    per_x = 2 * np.pi * x
    field_x = np.pi * x ** 2
    per_y = 2 * np.pi * y
    field_y = np.pi * y ** 2
    print("1st circle: \nPerimeter: " + str(per_x) + "   Field: " + str(field_x))
    print("2nd circle: \nPerimeter: " + str(per_y) + "   Field: " + str(field_y))
