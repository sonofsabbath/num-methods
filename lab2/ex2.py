for x in range(2, 100, 2):
    for y in range(2, x+1, 2):
        if x % y == 0:
            print("x: " + str(x) + " y: " + str(y))
