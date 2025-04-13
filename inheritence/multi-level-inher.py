class Car:
    @staticmethod
    def start():
        return "car started.."
    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesel")
print(car1.start())
print(car1.type)