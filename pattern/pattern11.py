def numPattern(num):
    for row in range(1, num):           
      for col in range(1, row + 1):  
        print(col, end='')         
      print() 
numPattern(6)