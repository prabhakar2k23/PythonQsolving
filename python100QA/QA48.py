funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])

# and now

funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])