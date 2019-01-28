# 30 m

##def pyth_tri(a, b, c):
##    text = "a Pythagorian Triple"
##    if a**2 + b**2 == c**2:
##        print "Is %s" % text
##    else:
##        print "Is not %s" % text
        
print "Welcome to Pythagorean triple checker"
# run forever
while True:
    
    # prompt user input
    user_input = raw_input("Please enter a triangle, A, B, C, as numbers, eg. 123: ")
    input_list = []

    # allow user input in any order
    
    # convert string to list of integers
    for character in user_input:
        input_list.append(int(character))
        
##    # validate integers (not working)
##    valid = input_list[0]
##    isinstance(int, valid)
        
    # assign variables for each integer
    a, b, c = input_list[0], input_list[1], input_list[2]
    #print a, b, c

    # set calculation order by largest number
    # swap variables without temp. var.
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > c:
        a, c = c, a

    # calculate pythagorean triple
    text = "a Pythagorian Triple"
    # right angled triangle
    if a**2 + b**2 == c**2:
        print "%s \nIs %s" % (user_input, text)
    else:
        print "%s \nIs not %s" % (user_input, text)
