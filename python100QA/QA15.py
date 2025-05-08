a=0
b=1
num = int(input("Enter the number to abtain fibonacci sequence: "))

if num == 1:
    print(0)
else:
    print(a)
    print(b)
    for i in range(1,num+1):
        c=a+b
        a=b
        b=c
        print(c)