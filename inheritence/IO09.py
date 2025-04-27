def magic(n, lst=[]):
    for i in range(n):
        lst.append(i*i)
    print(lst)

magic(2)
magic(3, [3, 2, 1])
magic(3)
