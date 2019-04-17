coins = 0
want_more = True

while want_more == True:
    print('You have %s coins.' % coins)
    ask = input('Do you want another? ')
    if ask == 'yes':
        coins += 1
    elif ask == 'no':
        print('Bye')
        want_more = False