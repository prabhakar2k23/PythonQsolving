num=68
result =[]
for i in range(1,num+1):
    if i%13==0:
        result.append(str(i))

res=[int(x) for x in result]
print(res)