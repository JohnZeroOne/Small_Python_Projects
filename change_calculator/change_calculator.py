#t 1h30
# could be improved a lot
# rounding floats is worse than using integers or decimals
# has a bug where change due is out by 1 cent
# uses inefficient way of calculating coins needed

def change_calc():

    ## money values
    #coin_list = [0.01, 0.05, 0.10, 0.25, 0.50, 1.00]
    # coin number
    cents, nickels, dimes, quarters, halfs, dollars = 0,0,0,0,0,0
    # coin value
    cent = 0.01
    nickel =  0.05
    dime = 0.10
    quarter = 0.25
    half = 0.50
    dollar = 1.00

    #change_is_due = 0

    print "Welcome to change calculator"

    
    try:
        item_cost = raw_input("Please enter the cost of the item: ")
        item_cost = float(item_cost)
        change_given = raw_input("Please enter the amount of money the customer has given: ")
        change_given = float(change_given)
    except:
        print "Please only enter numbers."
        change_calc()
    if item_cost > change_given:
        print "Customer has not given enough money."
        change_calc()
    change_due = round(change_given, 2) - round(item_cost, 2)
    change_due = round(change_due, 2)
    print "Change due: ", change_due

##    if change_due > 0:
##        change_is_due = 1
##        
##    while change_is_due:

    # very inefficient
    while change_due > dollar:
        change_due -= dollar
        dollars += 1
    while change_due > half:
        change_due -= half
        halfs += 1
    while change_due > quarter:
        change_due -= quarter
        quarters += 1
    while change_due > dime:
        change_due -= dime
        dimes += 1
    while change_due > nickel:
        change_due -= nickel
        nickels += 1
    while change_due > cent:
        change_due -= cent
        cents += 1
    #if round(change_due, 2) == 0.00:
    print "Coins needed: dollars: %s, halfs: %s, quarters: %s, dimes: %s, nickels: %s, cents: %s." % (dollars, halfs, quarters, dimes, nickels, cents)
    change_calc()
    
change_calc()
    
