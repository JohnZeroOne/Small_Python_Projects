# would've been simpler without a dictionary containing lists
# could clean up formatting for how the dict displays to users
# 90m
# make a dictionary containing
# key, item cost, item name

print "Welcome to menu calculator"

ordering = True

menu_list = [(1, (3.50,"Chicken Strips")),
             (2, (2.50,"French Fries")),
             (3, (4.00,"Hamburger")),
             (4, (3.50,"Hotdog")),
             (5, (1.75,"Large Drink")),
             (6, (1.50,"Medium Drink")),
             (7, (1.25,"Small Drink")),
             (8, (2.25,"Milk Shake")),
             (9, (3.75,"Salad"))]

menu_dict = dict(menu_list)

order_cost = 0

# loop to take multiple orders
while ordering:

    # print items and prices
    print "\n#, $,   item"

    for key, item in menu_dict.items():
        print "\n", key, item

    # take user input, string of numbers
    user_order = raw_input("\nPlease enter your order using the item #\n e.g: 12345: ")
    print "\n"
    
    # calculate cost of order
    # print how many of each item ordered and price
    for number in user_order:
    #print "number:", number
        for key, value in menu_dict.iteritems():
            #print key, value
            if int(key) == int(number):
                print key, value
                order_cost += value[0]

    # showing my workings
    # doesn't work for multiples of same item
##    for key, value in menu_dict.iteritems():
##        #print key, value
##        if str(key) in user_order:
##            print key, value
##            order_cost += value[0]
    #
##    for key, value in enumerate(menu_dict):
##        if str(key) in user_order:
##            print key, value
##            order_cost += value[0]
  
    # print total cost
    print "\nOrder cost: $", round(order_cost, 2)

    # let user order more
    user_choice = raw_input("\nDo you want to order again? (Y/N): ")
    if user_choice.upper() == "N":
        ordering = False
        #assert False
