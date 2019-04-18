import random

secret_number = random.randint(1,10)

play_again = True

print('I am thinking of a number between 1 and 10.')
while play_again:
    guessed_correctly = False
    guesses_allowed = 5
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
    
    y_or_no_check = False
    while y_or_no_check == False:
        ask_to_play_again = input('Do you want to play again(Y or N?) ')

        if(ask_to_play_again == 'N'):
            print('Bye!')
            play_again = False
            y_or_no_check = True
        elif(ask_to_play_again == 'Y'):
            y_or_no_check = True
