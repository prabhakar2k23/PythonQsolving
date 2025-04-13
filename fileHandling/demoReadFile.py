# f = open("demo.txt","r")
# data = f.readline()  # Read one line at a time
# print(data)

# data1= f.read()
# print(data1)
# f.close()     #close file

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)     # f.close() dene ki jarurat nahi with keuword automatic close kar deta hai

# Q1. Create a file "demo.txt"using python.Add the data
# with open("demo.txt","w") as f:
#     f.write("Hii everyone\nI am learning file i/o\nUsing Java.\nI like programming Java")


#Q2. WAP that replaces all occurences of "Java" with "Python" in above file.
# with open("demo.txt","r") as f:
#     data=f.read()
# data1=data.replace("Java","Python")
# print(data1)
# with open("demo.txt","w") as f:
#     f.write(data1)

#Q3. Search if the word "learning" exists in the file or not.
# with open("demo.txt","r") as f:
#     data = f.read()
#     word = "learning"
#     if(word in data):
#         print("Found")
#     else:
#         print("Not found")

#Q4. WAF to find in which line of the file does the word "learning" occur first.
# def fun():
#     line_no=1
#     word="Python"
#     data=True
#     with open("demo.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1   
# fun()

#Q5.From a file containing numbers separated by comma,print the count of even numbers.
count=0
with open("data.txt","r") as f:
    data=f.read()
    
    num= data.split(",")
    for val in num:
        if(int(val)%2==0):    
            count+=1
print(count)
