num1 = input("Enter a number : ")
length = len(num1)
c=0
for i in num1:
    c += int(i)**int(length)
if int(num1) == c:
    print(num1, "is a Armstrong number")
else:
    print(num1, "is not a Armstrong number")