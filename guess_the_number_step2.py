secret_number = 5
guessed_correctly = False
print('I am thinking of a number between 1 and 10.')

while guessed_correctly == False:
    get_number = int(input('What\'s the number? '))
    if get_number == secret_number:
        print('Yes! You win!')
        guessed_correctly = True
    elif get_number > secret_number:
        print('%d is too high' % get_number)
    else:
        print('%d is too low' % get_number)