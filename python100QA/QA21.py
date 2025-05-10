num = int(input("Enter a number: "))
print(num)

for i in range(1,num+1):
    print(i,end="")
    if i < num:
        print(",",end="")
print()
