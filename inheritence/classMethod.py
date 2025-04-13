class Person:
    name="anonymous"
    def changeName(self,name):
        #method1
        # Person.name = name
        
        #method2
        self.__class__.name=name

p1 = Person()
p1.changeName("Samrat Kumar")
print(p1.name)
print(Person.name)

