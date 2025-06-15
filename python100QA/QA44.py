def func():
    return [1, 2, 3], {'a': 4, 'b': 5}

lst, dct = func()
print(lst, dct)

# But now:
a, b = b, a = 1, 2
print(a, b)
