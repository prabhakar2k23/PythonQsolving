n=-17
if(n <= 1):
    for i in range(2,(n//2)+1):
       if(n%i==0):
           print(f"{n} is not a prime number")
           break
       else:
           print("prine number")
    else:
        print(f"{n} is not a prime number")