# notes
# 2h 
# wordlist uses a lot of words with uppercase first letter:
# having to use string.lower() method to make words match
#
# wordlist is long and makes the program slow to load first time

# randomly pick a word
import random
# read the word list online
import urllib2

def _init():
    # open the URL and set it as the wordlist locally
    wordlist = urllib2.urlopen("https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569").read()
    # split each word by new line
    wordlist = wordlist.split("\n")
    # test it works, very slow
    #print wordlist
    # welcome message
    print "Welcome to Hangman"
    print "To quit the game, when prompted type: 6\n"
    _main(wordlist)

def _main(wordlist):

    # select a random word from the list
    comp_word = random.choice(wordlist)
    comp_word = comp_word.lower()
    print "compword:", comp_word
    num_turns = 8
    user_word = []
    display_word = "_ " * len(comp_word)
    hangman = "-|-\n |\n\o/"

    # user still has turns
    while num_turns > 0:

        # prompt user to guess a word
        print "I have chosen a word it is %s letters long" % len(comp_word)
        print "Your word so far:", display_word
        print "You have %s guesses\n" % num_turns
        print hangman
        print user_word
        user_guess = raw_input("Please enter your guess: ")
        user_guess = user_guess.lower()
        # user quits
        if user_guess == "6":
            num_turns = 0
        # user must enter only 1 letter
        assert len(user_guess) == 1, "Guess should be 1 letter"
        # user guesses correctly
        if user_guess in comp_word:
            print "\nGood guess\n"
            # add guess to user word
            for position, letter in enumerate(comp_word):
                if letter == user_guess:
                    user_word[position] = letter
##            for user_guess in comp_word:
##                user_word += user_guess
            # check if words match
            _win(user_word, comp_word)
        else:
            num_turns -= 1
            print "\nThat letter is not in my word\n"
            # add piece to hangman
    
    _lose(comp_word)

def _lose(comp_word):
    # user runs out of turns
    print "Out of turns\nYou lose\nMy word was:", comp_word
    
def _win(user_word, comp_word):
    # user guesses entire word
    if user_word == comp_word:
            print "\nYou win!\nMy word was:", comp_word
            
_init()
