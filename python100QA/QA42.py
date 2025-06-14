class Bag:
    def __init__(self, items=[]):
        self.items = items

b1 = Bag()
b2 = Bag()

b1.items.append('apple')
b2.items.append('banana')

print("b1:", b1.items)
print("b2:", b2.items)