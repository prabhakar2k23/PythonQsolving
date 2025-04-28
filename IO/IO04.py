try:
    number = int(input("Enter a number: "))
    print("Square of the number:", number**2)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("Thank you for using the program.")
