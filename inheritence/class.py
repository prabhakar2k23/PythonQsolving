class Student:
    college="BCET"
    name="anonymous"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
    
    def hello(self):
        print(f"Hello {self.name}")

s1=Student("sk",97)
s1.hello()

