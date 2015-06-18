#Version 1.1 of guessing game (played from the command line)
#This version of the game allows users to guess numbers from 1 to 1,000, as opposed to 1 to 100. 

from random import randint;


        
def get_input(minAllowed = float("-inf"), maxAllowed = float("inf")):
   ''' This method returns a number which is gotten from the user within an interval [min, max] that can be specified by the caller.
   If no value is given by the caller, then the method takes numbers in the boundary [-infinity, +infinity] '''

   done = False;
   response = 0;
   while done == False:
         try:
               text = "Please enter a number between {minNum} and {maxNum}: ".format(minNum = minAllowed, maxNum = maxAllowed);
               val = raw_input(text);
               response = int(val)
               if (response >= minAllowed and response <= maxAllowed):
                  #then we have a valid number
                  done = True;
         except:
               print "Sorry, the input you entered was invalid."
   return response;

def play_game():
    """This is the main method for the game."""

    true_val = randint(1, 1000)
    guess = get_input(1, 1000)
    if (guess == true_val):
        print "Your guess was correct! Congratulations! You win!"
    elif (guess != true_val):
        print "Sorry, but your guess was incorrect.\nThe correct number is {ans}. You lost.".format(ans = true_val);



play_game();
