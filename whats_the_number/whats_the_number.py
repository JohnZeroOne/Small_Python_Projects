# t 110m

def findthenumber():

    # between 1 and 1000
    for i in xrange(1, 1001):
        #print "Between 1 and 1000"
        # has two or more digits
        if has_two_more_digit(str(i)):
            #print "Has two or more digits"
            # is prime
            if isprime(i):
                #print "Is a prime number"
                # does not contain a 1 or 7
                if not_1_or_7(i):
                    #print "does not contain a 1 or 7"
                    # sum of all digits less than or equal 10
                    if sum_ten(i):
                        #print "sum of digits 10 or less"
                        # sum of first two digits is odd
                        if first_odd(i):
                            #print "sum of first two digits is odd"
                            # second to last digit is even
                            if second_last_odd(i):
                                #print "second to last digit is even"
                                # last digit is equal to total number of digits
                                if last_digit(i):
                                    #print "last digit is equal to total number of digits"
                                    print "The number is", i
                            
                        

def has_two_more_digit(num):
    """
        returns true if input has 2 or more digits
        otherwise returns false
    """
    if len(num) > 2:
        return True
    else:
        return False

# check if a number is one of the first 1000 primes
def isprime(num):
    """
        Input: any positive integer up to 1000
        checks integer against list of known primes
        Returns: True if in list otherwise False
    """
    # found list online and formatted using str.split() method
    prime_list = ['2', '3', '5', '7', '11', '13', '17',
                  '19', '23', '29', '31', '37', '41',
                  '43', '47', '53', '59', '61', '67',
                  '71', '73', '79', '83', '89', '97',
                  '101', '103', '107', '109', '113',
                  '127', '131', '137', '139', '149',
                  '151', '157', '163', '167', '173',
                  '179', '181', '191', '193', '197',
                  '199', '211', '223', '227', '229',
                  '233', '239', '241', '251', '257',
                  '263', '269', '271', '277', '281',
                  '283', '293', '307', '311', '313',
                  '317', '331', '337', '347', '349',
                  '353', '359', '367', '373', '379',
                  '383', '389', '397', '401', '409',
                  '419', '421', '431', '433', '439',
                  '443', '449', '457', '461', '463',
                  '467', '479', '487', '491', '499',
                  '503', '509', '521', '523', '541',
                  '547', '557', '563', '569', '571',
                  '577', '587', '593', '599', '601',
                  '607', '613', '617', '619', '631',
                  '641', '643', '647', '653', '659',
                  '661', '673', '677', '683', '691',
                  '701', '709', '719', '727', '733',
                  '739', '743', '751', '757', '761',
                  '769', '773', '787', '797', '809',
                  '811', '821', '823', '827', '829',
                  '839', '853', '857', '859', '863',
                  '877', '881', '883', '887', '907',
                  '911', '919', '929', '937', '941',
                  '947', '953', '967', '971', '977',
                  '983', '991', '997']
    # check if number is in the list of primes
    if str(num) in prime_list:
        #print "num in prime list"
        return True
    else:
        #print "not in prime list"
        return False

def not_1_or_7(num):
    """
        checks the digits in the input number
        when it finds a 1 or 7 returns false
        otherwise returns true
    """
    # check each digit for 1 or 7
    for digit in str(num):
        if digit == "1" or digit == "7":
            return False
    return True

def sum_ten(num):
    """
        returns True if the sum of digits
        in the input are 10 or less
        otherwise returns False
    """
    sum_of_digits = 0

    #print "start, sum digits", sum_of_digits

    # add all digits together
    for digit in str(num):
        #print "for, sum digits", sum_of_digits
        sum_of_digits += int(digit)
    # check if it's 10 or less
    if sum_of_digits <= 10:
        return True
    else:
        #print "false, sum digits", sum_of_digits
        return False

def first_odd(num):
    """
        returns True if the sum of the
        first two digits in the input are odd
        otherwise returns False
    """
    
    sum_of_digits = 0
    # get the first digit
    # convert to string and slice the first digit
    digit1 = str(num)
    
    # error check
##    print "digit1:", digit1
##    if isinstance(digit1, str):
##        print "digit1 is a string"
##    else:
##        print "digit1 is not a string"
    
    digit1 = digit1[0]
    # convert to string and slice the second digit
    digit2 = str(num)
    digit2 = digit2[1]
    # convert back to integer and add together
    sum_of_digits = int(digit1) + int(digit2)
    # check if this sum produces an even number
    if sum_of_digits % 2 != 0:
        return True
    else:
        return False

def second_last_odd(num):
    """
        returns True if the
        second last digit is even
        otherwise returns False
    """

    # convert to string and slice to get the second last digit
    second_last = str(num)
    second_last = second_last[-2]
    # convert to integer for our check
    # check if this is an even number
    if int(second_last) % 2 == 0:
        return True
    else:
        return False

def last_digit(num):
    """
        returns True if the last digit
        is equal to the total number of digits
        e.g: last_digit(12345) returns True
        otherwise returns False
    """
    num_digits = 0
    #print "num_digits:", num_digits

    # convert to string and slice to get the last digit
    last_num = str(num)
    last_num = last_num[-1]
    #print "last_num:", last_num
    
    # count how many digits there are
    for digit in str(num):
        num_digits += 1
    #print "num_digits:", num_digits
        
    # check for equality between number of digits and last number
    if num_digits == int(last_num):
        return True
    else:
        return False
