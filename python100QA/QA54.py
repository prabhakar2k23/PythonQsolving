class Callable:
    def __call__(self, x):
        print(f"Called with {x}")

obj = Callable()
obj(10)

print(callable(obj))
print(callable(obj.__call__))