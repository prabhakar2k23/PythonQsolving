class Person:
    name="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1 = Person()
p1.changeName("Samrat Kumar")
print(p1.name)
print(Person.name)