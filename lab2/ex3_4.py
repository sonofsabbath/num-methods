from cs50 import get_float, get_int

x = get_float("x: ")
y = get_float("y: ")

if y == 0:
    print("You can't divide by 0")
    quit()

divisible = "x is divisible by y" if x % y == 0 else "x is not divisible by y"
print(divisible)

prec = get_int("Decimals: ")  # ex4
if prec < 0:
    print("Number of decimals must be higher than zero")
    quit()
else:
    r = "{0:." + str(prec) + "f}"
    div = r.format(x / y)

print("x/y = " + div)
