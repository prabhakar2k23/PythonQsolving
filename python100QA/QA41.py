class Weird:
    def __new__(cls):
        print("In __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("In __init__")

class Cancelled:
    def __new__(cls):
        print("Cancelled creation!")
        return None

    def __init__(self):
        print("You’ll never see this.")

w = Weird()
c = Cancelled()
print(w)
print(c)
