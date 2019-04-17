width = int(input('Width? '))
height = int(input('Height? '))

count = 0

while count < height:
    if (count == 0) or (count == (height-1)):
        print('*' * width)
    else:
        print('*' + ' ' * (width-2) + '*')
    count += 1