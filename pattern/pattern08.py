width = 5
height = 5

for i in range(height):
    if i == 0 or i == height - 1:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')
