rows = int(input("How many rows do you want in the hollow pyramid? "))

i = 1
while i <= rows:
    space = 0
    while space < rows - i:
        print(" ", end="")
        space += 1
    k = 0
    while k < (2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
        k += 1
    print()
    i += 1
