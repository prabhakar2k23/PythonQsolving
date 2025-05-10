nterms= int(input("Enter number of terms here: "))
results=[]
for i in range(nterms+1):
    result=2**i
    results.append(result)
print(results)