#t 5m

def factors_(num):
    """
        Input: num, a positive integer
        Returns: num and all factors of num, ascending order
    """
    # store factors in a list
    factor_list = []
    # check for positive factors up to user's number
    for i in xrange(1, num+1):
        if num % i == 0:
            factor_list.append(i)
    # return list of factors
    return factor_list
