n=int(input("Enter a numbar: "))
mul=1

for i in range(1,n+1):        #bydefault i start from 0 so you must set the value of i=1 in range parameter
    mul *= i
print(f"Multiplication of 1 to {n} = {mul}")