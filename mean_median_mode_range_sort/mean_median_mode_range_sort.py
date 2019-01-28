# t 120m

#from math import floor
#import decimal

def sort_num(number_list):
    """
    Input: list of numbers e.g [1, 2, 3, 0]
    Returns: numbers sorted into numerical order in a list
    """
##    # manual selection sort not finished
##    highest = 0
##    for number in number_list:
##        if number > highest:
##             number_list.append(number)
    
    # use in-built sorting algorithm
    number_list = sorted(number_list)
    return number_list
    
def mean(number_list):
    """
    Input: list of numbers e.g [1, 2, 3]
    allows user to select how many decimal
    points they want to round to
    Returns: approximate mean average of input
    """
    # temporarily store a sum of and how many numbers were input
    sum_numbers = 0.0
    number_instances = 0.0

    decimal_place = raw_input("Select how many decimal points you want to round the answer to: ")
    decimal_place = int(decimal_place)
    # add all numbers in the list
    # count how many numbers occurred
    for number in number_list:
        sum_numbers += number
        number_instances += 1

    print "dec. place:", decimal_place
    # return the numbers divided by occurrances
    #result = decimal.Decimal(str(sum_numbers)) / decimal.Decimal(str(number_instances))
    result = sum_numbers / number_instances
    # BUG rounding bug with all but 3, 5, 8, 9
    result = round(result, decimal_place)
    #result = floor(result)
    return result

def median(number_list):
    """
    Input: list of numbers e.g [1, 2, 3]
    Returns: the middle number
    or for even inputs, the two numbers in the middle
    """
    # sort list numerically
    number_list = sort_num(number_list)
    
    number_instances = 0
    # count how many numbers were input
    for number in number_list:
        number_instances +=1
        
##    # if its even return the mean of both middle values
##    if number_instances % 2 == 0:
##        # find the middle
##        middle = number_instances / 2
##        return mean(number_list[middle-1:middle+1])
##    

    # if its even return both middle values
    if number_instances % 2 == 0:
        # find the middle
        middle = number_instances / 2
        middle = number_list[middle-1:middle+1]
        #print "middle:", middle
        #assert False
        return middle
    else:   
        # find the middle
        middle = number_instances / 2
        # return the middle number
        return number_list[middle]

def mode(number_list):
    """
    Input: list of numbers e.g: [1, 1, 2, 3]
    Returns: most frequently occurring number e.g: 1
    or None if there isn't one
    """
    # list comprehension
    # count numbers and occurrence in a list of lists
    freq_list = [[x, number_list.count(x)] for x in set(number_list)]
    # save highest number
    highest =  0
    highest_list = []
    # calculate the highest number in the list
    for val1, val2 in freq_list:
        #print "val1, val2:", val1, val2
        if val2 > highest:
            highest = val2
            highest_list = [val1, val2]
    # return the most frequently occurring number
    return highest_list[0]

def _range(number_list):
    """
    Input: list of numbers e.g: [1, 2, 3]
    Returns: the range of the numbers in the list e.g: 3
    """
    # sort list numerically
    number_list = sort_num(number_list)
    #print "numlist:", number_list
    
    # subtract the last number from the first number in the list
    return number_list[-1] - number_list[0]
