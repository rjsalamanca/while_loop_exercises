left = 1

while left <= 10:
    right = 1

    while right <= 10:
        total = left * right
        print('%d X %d = %d' % (left,right,total))
        right += 1
    left += 1