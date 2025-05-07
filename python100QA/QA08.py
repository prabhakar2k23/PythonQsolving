num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
num3=int(input("Enter Third Number: "))

if num1>num2>num3:
    print(f"{num1} is Greater!")
elif num2>num3:
    print(f"{num2} is Greater!")
else:
    print(f"{num3} is Greater!")