class Descriptor:
    def __get__(self, obj, objtype=None):
        print("Getting value")
        return 42

    def __set__(self, obj, value):
        print(f"Setting value to {value}")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)
obj.attr = 100
print(obj.attr)
