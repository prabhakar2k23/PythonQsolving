year=int(input("Enter the year to check leap year or not: "))
if (year%4==0) and (year%100!=0 or year%400==0):
    print(f"{year} is Leap year.")
else:
    print(f"{year} is not leap year.")