num=int(input("Enter a number: "))
sum=0

if num<=0:
    print("Enter positive number")
else:
    while num>0:
        sum += num
        num -= 1
print(sum)