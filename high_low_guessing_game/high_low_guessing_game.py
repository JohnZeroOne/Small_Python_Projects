# t 30m

#t 30
# used to calulate pseudo-random numbers
import random
# delay computer guesses
import time

# welcome msg
print """
         Welcome to high-low a guessing game\n
         I will select a number at random from 0 to 100\n
         You should try to guess my number when prompted\n
         If you get it wrong I will tell you if my number is higher or lower\n
         Let's begin!
      """

def high_low():
    """
        main game function, contains all game logic to let the user play
    """
    # flag to keep playing
    user_playing = True
    # generate a pseudo-random number
    computer_answer = random.randrange(0, 100)
    #print "comp ans:", computer_answer
    # log user guesses
    num_guesses = 1
    
    while user_playing:
        #computer_answer = 0
        # store the user's guess number
        user_guess = raw_input("Please enter your guess from 0 to 100: ")
        user_guess = int(user_guess)
        # user guesses correctly
        if user_guess == computer_answer:
            print "Congratulations you guessed my number!"
            # use correct grammar
            guess_word = "guesses"
            if num_guesses == 1:
                guess_word = "guess"
            # show guesses taken
            print "It took you %s %s\n" % (num_guesses, guess_word)
            # does the user want to play again?
            try:
                play_again = raw_input("Play again? (Y/N) ")
                play_again = play_again.upper()
                #print "playagain:", play_again
                if play_again == "N":
                    #user_playing = False
                    print "Thank you for playing\n"
                    return None
                    break
                else:
                    print "Restarting..\n"
                    high_low()
            # user enters bad input
            except:
                print "Invalid input, restarting game..\n"
                high_low()
        # user guess is less than the right answer
        elif user_guess < computer_answer:
            num_guesses += 1
            print "My answer is higher\n"
        # user guess is more than the right answer
        elif user_guess > computer_answer:
            num_guesses += 1
            print "My answer is lower\n"



def comp_guess():
    """
        makes the computer play the game using binary/bisection search algorithm
    """
    # flag for correct answer
    wrong_answer = True

    # range for guesses
    high = 100
    low = 0
    # guess average/middle of search space
    guess = (high + low) / 2
    answer = random.randrange(low, high)

    #print "answer:", answer
    
    # loop until we find the answer
    while wrong_answer:
        # guess is correct
        if guess == answer:
            time.sleep(1)
            print "Correct:", guess
            wrong_answer = False
        # guess is too low
        elif answer > guess:
            time.sleep(1)
            print "Too low:", guess
            # eliminate low search space
            low = guess +1
            guess = (high + low) / 2 
        # guess is too high
        else:
            time.sleep(1)
            print "Too high:", guess
            # eliminate high search space
            high = guess -1
            guess = (high + low) / 2 

    print "Win!"
    
# start the game
#high_low()
_play = raw_input("Enter 1 to play the game: ")
if _play == "1":
    high_low()
