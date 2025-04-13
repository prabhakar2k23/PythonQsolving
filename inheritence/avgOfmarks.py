class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg(self):
        sum=0
        for val in self.marks:
            sum += val
            avg=sum/len(self.marks)
        print(f"Hello {self.name} your avg of marks is: {int(avg)}")

s1=Student("Samrat",[98,78,90])
s1.avg()