# DEV NOTES
# 1h
# could save stats between games
# could run in a while loop rather than function call
# error correction could be more robust


# random used to generate numbers
import random
print "Welcome to dice game."
##
##while True:
##    raw_input("Press enter to roll a dice ")
##    print random.randrange(1, 7, 1)

# main game function
def diceroll():
    # save our user input
    try:
        dice_sides = raw_input("Please enter the number of sides of the dice: ")
        roll_times = raw_input("Please enter the number of times you want to roll: ")
        dice_sides = int(dice_sides) +1
        roll_times = int(roll_times)
        list_stats = []
    except:
        print "Please type in a single number, only!"
        diceroll()

    # roll the dice x times
    for i in range(roll_times):
        # generate random rolls
        try:
            num = random.randrange(1, dice_sides, 1)
            list_stats.append(num)
            print num
            #print "Dice stats:", list_stats
        # user input caused error, restart
        except:
            pass
            print "Invalid input, try again with numbers only"
            diceroll()

    # prompt user to see statistics  
    user_stat = raw_input("Do you want to see stats, Y/N: ")
    assert isinstance(user_stat, str), "input must be a string 'Y or N'"
    user_stat = user_stat.upper()
    if user_stat == "Y":
        user_num = raw_input("Enter the number you would like to see stats for: ")
        user_num = int(user_num)
        number = 0
        # count the occurrences of users number
        for i in list_stats:
            if i is user_num:
                number +=1
        percent = float(number) / float(roll_times) * 100.0
        print "percent, number, roll_times", percent, number, roll_times
        print "Number", user_num,"has rolled", number,"time(s)", percent, "%"
    # end of rolls
    diceroll()

#start the game
diceroll()
