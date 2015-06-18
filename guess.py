#This is a numbers guessing game (played from the command line)


from random import randint, choice;

class GuessingGame:

    def __init__(self, limit):
       limit = max(100, limit); #this ensures that the limit is always >= 100. 
       self.limit = limit; #the limit is the highest valid  guess
       self.trueNum = 0; #this is the true value that the player is trying to guess
                         #it's default value is 0. 
       self.triesLeft = max(3, min(12, limit/200)); #based on the limit, you get a certain amount of tries to guess the correct number,
                                                    #however, you cannot get more than 12 tries no matter how big your guessing range is.
       self.score = 0;
       self.rounds = 5;
       
    def get_input(self, minAllowed = float("-inf"), maxAllowed = float("inf")):
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

    def display_hint(self, guess):
       #''' Based on the player's input, we give info that might help in guessing the true number'''

       if (guess < self.trueNum):
          #then we know that the player needs to increase his/her number
          possibleResponses = ["Your guess is too low\n", "You might want to increase your guess\n", "Hmmm...your guess is low. Maybe you should try increasing it.\n"]
          print (choice(possibleResponses))
       elif (guess > self.trueNum):
          #then we know that the player needs to decrease his/her number
          possibleResponses = ["Friend, your guess is too high!\n", "Maybe you should try a smaller number; the one you entered is too large\n", "You might want to reduce that number\n"]
          print (choice(possibleResponses))

    def play_game(self):
        ''' This is the main method of the Guessing Game class. '''
        
        for i in range(1, self.rounds + 1): #this means we play for x times (where x is self.rounds)
                                            #we have self.rounds + 1 because range(min, max) only goes up to max - 1, and we want it to go to max. 
           if (i == self.rounds):
              print ("Please note that this is your last round! Let's make it count!")
           else :
              print ("Number of rounds left: {val}".format(val = self.rounds + 1 - i))

           self.single_round();
           print "Your score is {score}  out of {total}\n".format(score = self.score, total = i); #i represents the number of rounds currently played. 
         

    def single_round(self):
        '''This method is responsible for coordinating a single round of the game.'''
        self.trueNum = randint(1, self.limit);
        numberGuessed = False;
        currentGuesses = []; #this array stores the guesses that the player has made. It is initially empty
        originalNumTries = self.triesLeft; #this is the original amount of tries you get to guess a number. 
        while (self.triesLeft > 0):
              guess = self.get_input(1, self.limit)
              if (guess == self.trueNum):
                    self.score = self.score + 1;
                    print ("Congratulations! You guessed the correct number!")
                    numberGuessed = True;
                    #We can now exit the loop since the player has guessed the correct number
                    break;
              else:

                    self.triesLeft = self.triesLeft - 1; #we reduce the number of tries left because the player didn't guess correctly

                    if self.triesLeft > 0: #this if statement ensures that hints are only given to people who still have some tries left. 

                        if guess in currentGuesses:
                            print "Friend, you've guessed this number before, and it isn't correct"
                        else:
                            currentGuesses.append(guess); #add the user's guess to a list.
                                                          #this allows to tell them if they've guessed a number more than once. 
                        self.display_hint(guess) #displays a hint based on the user's guess.
                    
                    #we display a message based on how many tries are left for the player.
                    if (self.triesLeft > 1): 
                         print ("You have {val} tries left".format(val = self.triesLeft))
                    elif (self.triesLeft == 1):
                       print ("You have just one try left! You've got to make it count! But hey, no pressure! :-D")

                                        

        if (numberGuessed == False): #then the player didn't guess the correct number before running out of chances to do so.
            print ("Sorry, but you're out of turns and you didn't guess the correct answer. The computer's guess was actually {answer}").format(answer = self.trueNum);
              
        #then we set the number of tries back to its original value.
        self.triesLeft = originalNumTries;
        print ("\n")


def __main__():
      game = GuessingGame(700); #initialize the game with the guessing limit
      game.play_game(); #start the game

if (__name__ == "__main__"):
    __main__()
