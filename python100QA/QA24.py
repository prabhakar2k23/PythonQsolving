num=68
for i in range(1, num+1):
    if i % 13 == 0:
        if i + 13 < num:
            print(i, end=", ")
        else:
            print(i, end="")
