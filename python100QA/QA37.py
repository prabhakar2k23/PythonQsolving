functions = []
for i in range(3):
    def f():
        return i
    functions.append(f)

results = [func() for func in functions]
print(results)
