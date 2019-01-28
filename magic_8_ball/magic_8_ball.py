# DEV NOTES
# 15m
#
# store reponses in separate text file
# add GUI
# add error correction on user input
#

# random answers
import random
# delay
import time

# starting message
print "Welcome to magic 8 ball"
print "I will answer your questions"

# play flag
playing = True

# play the game until user quits
while playing == True:
    raw_input("Ask me a yes or no question: ")
    print "Thinking..."
    time.sleep(3)
    reponse_list = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]

    random_response = random.randint(0, 20)
    print reponse_list[random_response]
    
    #prompt user, if they want to play
    user_play = raw_input("Play again(Y/N)? ")
    if user_play.upper() == "N":
        playing = False
