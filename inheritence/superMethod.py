class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name

car1=ToyotaCar("prius","electric")
print(car1.name)
print(car1.type)