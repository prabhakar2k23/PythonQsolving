number = int(input("Enter a number to generate its multiplication table: "))

def multiplication_table(n):
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(number)
