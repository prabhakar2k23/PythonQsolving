for num in range(1, 101):
    if num <= 1:
        continue
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            break
    else:
        print(num,end=" ")
