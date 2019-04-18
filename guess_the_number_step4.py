import random

secret_number = random.randint(1,10)
guessed_correctly = False
guesses_allowed = 5
print('I am thinking of a number between 1 and 10.')

while guessed_correctly == False and guesses_allowed > 0:
    print('You have %d guesses left.' % guesses_allowed)
    guesses_allowed -= 1
    get_number = int(input('What\'s the number? '))
    if get_number == secret_number:
        print('Yes! You win!')
        guessed_correctly = True
    elif get_number > secret_number:
        print('%d is too high' % get_number)
    else:
        print('%d is too low' % get_number)
if guesses_allowed == 0 and guessed_correctly == False:
    print('You ran out of guesses!')