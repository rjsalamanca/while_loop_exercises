triangleHeight = 4
count = 0
stars = '*'

while count < triangleHeight:
    spaces = triangleHeight - count
    print(' ' * spaces + stars)
    count += 1
    stars += '**'