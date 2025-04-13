# Write a Python program to find the index of a particular element in a list

list1 = [10,20,30,40,50,60,70,80]

def fun(li,el):
    for i in range(len(li)):
        if li[i]==el:
            return f"{el} found at index: {i}"
    return "element not found"
    
index=fun(list1,70)
print(index)
