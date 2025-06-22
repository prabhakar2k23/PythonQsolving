def gen():
    val = yield 1
    yield val

g = gen()
print(next(g))     # → 1
print(g.send(42))  # → 42
