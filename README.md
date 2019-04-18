# while_loop_exercises

## Exercise Below is stored in loop_1_to_10.py

1 to 10


Using a while loop, print out the numbers between 1 and 10 inclusive, one on a line. Example output:

$ python loop_1_to_10.py
```
1
2
3
4
5
6
7
8
9
10
```

## Exercise Below is stored in loop_n_to_m.py

n to m


Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:

$ python loop_n_to_m.py
```
Start from: 2
End on: 8
2
3
4
5
6
7
8
```

## Exercise Below is stored in loop_odd_numbers.py

Odd Numbers


Print each odd number between 1 and 10 inclusive. Example output:

$ python loop_odd_numbers.py
```
1
3
5
7
9
```
Hint: you will need to use the modulus operator % to determine whether a number is odd or even.

## Exercise Below is stored in loop_coins_boolean.py
How many coins?


Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:

$ python loop_coins_boolean.py
```
You have 0 coins.
Do you want another? yes
You have 1 coins.
Do you want another? yes
You have 2 coins.
Do you want another? no
Bye
```

## Exercise Below is stored in loop_5x5_square.py

Print a Square


Print a 5x5 square of * characters. Example output:

$ python loop_5x5_square.py
```
*****
*****
*****
*****
*****
```
## Exercise Below is stored in loop_NxN_square.py

Print a Square II


Print a NxN square of * characters. Prompt the user for N. Example output:

$ python loop_NxN_square.py
How big is the square? 10
```
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
```

## Exercise Below is stored in loop_print_box.py

Print a Box


Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

$ python loop_print_box.py
Width? 6
Height? 4
```
******
*    *
*    *
******
```

## Exercise Below is stored in loop_triangle.py

Print a Triangle


Print a triangle consisting of * characters like this:
```
   *
  ***
 *****
*******
```

## Exercise Below is stored in loop_triangle_2.py

Print a Triangle II

Given a number as the height, print a triangle as in "Print a Triangle" but with the given height. Example:

$ python loop_triangle_2.py
```
Triangle Height: 20
                    *
                   ***
                  *****
                 *******
                *********
               ***********
              *************
             ***************
            *****************
           *******************
          *********************
         ***********************
        *************************
       ***************************
      *****************************
     *******************************
    *********************************
   ***********************************
  *************************************
 ***************************************
```

## Exercise Below is stored in loop_multiplications_table.py

Multiplication Table


Print the multiplication table for numbers from 1 up to 10. Example output:

$ python multiplication_table.py
```
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
1 X 4 = 4
...
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
...
10 X 8 = 80
10 X 9 = 90
10 X 10 = 100
```

## Exercise Below is stored in loop_banner.py

Bonus: Print a Banner


Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. Example session:

$ python loop_banner.py
Text? Welcome to DigitalCrafts
```
****************************
* Welcome to DigitalCrafts *
****************************
```

## Exercise Below is stored in loop_triangle_number_sequence.py

Bonus: Triangle Numbers


Print the first 100 triangle numbers. What is a triangle number? Read this: https://www.mathsisfun.com/algebra/triangular-numbers.html.

## Exercise Below is stored in loop_factors.py

Bonus: Factor a Number


Given a number, print its factors. What are factors? https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-and-factors/v/finding-factors-of-a-number



## Additional While Loop Exercises (Blast off)

## Exercise Below is stored in blastoff.py

Blastoff

Similar to your 1 to 10 counter, write a program that counts down:
```
$ python blastoff.py
10
9
8
7
6
5
4
3
2
1
0
```
## Exercise Below is stored in blastoff_2.py

**Blastoff 2**

Modify blastoff so that it prints a custom message once it gets to 0.

## Exercise Below is stored in blastoff_3.py

**Blastoff 3**

Prompt the user for the number to start counting from.

## Exercise Below is stored in blastoff_4.py

**Blastoff 4**

Now, make sure the user doesn't enter a number larger than 20

## Exercise Below is stored in blastoff_5.py

**Blastoff 5**

Make blastoff wait one second before proceeding to the next number.
Hint: check out the docs for the time module.

 ## Additional While Loop Exercises (Guess a Number)

 ## Exercise Below is stored in guess_the_number.py

**Step 1**

You will implement a guess-the-number game where the player has to try guessing a secret number until he gets it right. For now, you will "hard code" the secret number to 5 (just set it to five like secret_number = 5). You will prompt the player to enter a number again and again, each time comparing his input to the secret number. To to that, you will need to write a while loop. If he guesses correctly, you will print "You win!", otherwise, you will prompt for a number again.

Example session:

```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
What's the number? 3
Nope, try again.
What's the number? 9
Nope, try again.
What's the number? 5
Yes! You win!
```

 ## Exercise Below is stored in guess_the_number_step_2.py

**Step 2: Give High-Low Hint**

Improve your game to provide the player with a high-or-low hint. Example session:

```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
What's the number? 3
3 is too low.
What's the number? 9
9 is too high.
What's the number? 5
Yes! You win!
```

 ## Exercise Below is stored in guess_the_number_step_3.py

**Step 3: Randomly Generated Secret Number**

Instead of hard-coding the secret number to 5 now, you will generate the secret number using a random number generator provided by Python, so that even you, the programmer, cannot know the secret number before hand. To generate a random number between 1 and 10, inclusive, do this:

import random
my_random_number = random.randint(1, 10)
Use this same method to generate your secret number for the game. Play the game a couple of times to see that the secret number is different each time.

 ## Exercise Below is stored in guess_the_number_step_4.py

**Step 4: Limit Number of Guesses**

Limit the number of guesses the player has to 5. If he cannot guess the number within 5 guesses, he losses.

 Example session:

```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
You have 5 guesses left.
What's the number? 1
1 is too low.
You have 4 guesses left.
What's the number? 10
10 is too high.
You have 3 guesses left.
What's the number? 2
2 is too low.
You have 2 guesses left.
What's the number? 7
7 is too high.
You have 1 guesses left.
What's the number? 4
4 is too low.
You ran out of guesses!
```

 ## Exercise Below is stored in guess_the_number_play_again.py

**Bonus: Play Again**

At the conclusion of a game, give the player the option of playing again. Example session:

```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
You have 5 guesses left.
What's the number? 1
Yes! You win!
Do you want to play again (Y or N)? Y
I am thinking of a number between 1 and 10.
You have 5 guesses left.
What's the number? 5
Yes! You win!
Do you want to play again (Y or N)? N
Bye!
```