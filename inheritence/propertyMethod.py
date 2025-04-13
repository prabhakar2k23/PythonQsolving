#normal method
# class Student:
#     def __init__(self,phy,chem,math):
#         self.physics=phy
#         self.chemestry=chem
#         self.math=math
#     def calculatePerc(self):
#         self.percentage= str((self.physics + self.chemestry + self.math)/3) + "%"

# s1=Student(98,97,99)
# s1.calculatePerc()
# print(s1.percentage)
# s1.physics=80
# s1.calculatePerc()
# print(s1.percentage)


# with @property decorator
class Student:
    def __init__(self,phy,chem,math):
        self.physics=phy
        self.chemestry=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.physics + self.chemestry + self.math)/3) + "%"

s1=Student(98,97,99)

print(s1.percentage)
s1.physics=80
print(s1.percentage)
s1.math=80
print(s1.percentage)
