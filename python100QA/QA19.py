num=int(input("Enter a number "))

sum=0
if num<=0:
    print("Please enter positive number")
else:
    for i in range(num+1):
        sum += i

print(sum)