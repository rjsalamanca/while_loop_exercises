find_factors = int(input('Find all the factors of: '))

factors = ''

count = 1

while count <= find_factors:
    countRightSide = 1
    while countRightSide <= find_factors:
        equals_find_factors = count * countRightSide
        if(equals_find_factors == find_factors):
            factors += ('%d ' % count)
        countRightSide += 1
    count += 1

print(factors)