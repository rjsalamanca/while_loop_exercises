triangle = 1
while triangle <= 10:
    count = 0
    stars = '*'
    countStars = 0

    while count < triangle:
        spaces = triangle - count
        print(' ' * spaces + stars)
        count += 1
        countStars += count
        stars += ' *'

    triangle += 1
    print(countStars)