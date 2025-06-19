def gen():
    val = yield 1
    yield val

g = gen()
print(next(g))
print(g.send(42))