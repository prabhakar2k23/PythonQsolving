def addNumbers(num1,num2):
    try:
        return (num1 / num2)
    except IndexError:
        return ('Invalid Index')
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero!")
    except Exception as e:
        return e
       
print(addNumbers(7,1))
print("End of code")