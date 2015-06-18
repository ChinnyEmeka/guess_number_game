#Version 1.0
#This is a guessing game. You play it from the command line.

from random import randint;

def get_number():
    true_val = randint(1, 100)
    guess = raw_input("The computer has chosen a number between 1 and 100.\nPlease enter your guess: ")
    if (guess == true_val):
        print "Your guess was correct! Congratulations! You win!"
    elif (guess != true_val):
        print """Sorry, but your guess was incorrect.\nThe correct number is {ans}. You lost.""".format(ans = true_val);
        
get_number();
