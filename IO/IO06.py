try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Please enter a number")
else:
    print(result)
    
