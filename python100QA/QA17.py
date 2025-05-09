# Check given number is Armstrong or not
num = int(input("Enter a 3 digit number"))

sum = 0
temp = num

while temp > 0:
    digit = temp%10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10

if sum == num:
    print("It is an armstrong number")
else:
    print("Not a armstrong number")