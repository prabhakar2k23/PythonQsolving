#Inheritence:- When one class derives the properties of another class.
# It's called single inheritence
class Car:
    color="blue"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1= ToyotaCar("fortuner")
car2= ToyotaCar("lamborgini")

print(car1.name)
print(car1.start())
print(car2.color)