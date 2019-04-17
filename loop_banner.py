banner = input('Text? ')
lines = 0

while lines < 3:
    if lines == 1:
        print( '* ' + banner + ' *')
    else:
        print('*' * (len(banner)+4))
    lines += 1