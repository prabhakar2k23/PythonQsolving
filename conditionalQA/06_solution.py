n=6
fac=1
# for i in range(1,n+1):
#     fac *= i
# print(fac)

while n > 0:
    fac *= n
    n-=1
print(fac)