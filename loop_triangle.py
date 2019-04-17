triangleHeight = int(input('Triangle Height: '))
count = 0
stars = '*'

while count < triangleHeight:
    spaces = triangleHeight - count
    print(' ' * spaces + stars)
    count += 1
    stars += '**'