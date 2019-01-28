#t 1h

# define coins
class coin:
    """monetary unit covering all coin types"""
    coinCount = 0
    
    def __init__(self, cointype, weight, wrapper, value):
        self.cointype = cointype
        self.weight = weight
        self.wrapper = wrapper
        self.value = value
        coin.coinCount += 1

    def cointype(self):
        return self.cointype

# different coin types
# inherit from coins
class cent(coin):
    weight = 2.500
    value = 0.01
    wrapper = 50
    
#class penny(cent):
    
class nickel(coin):
    weight = 5.000
    value = 0.05
    wrapper = 40

class dime(coin):
    weight = 2.268
    value = 0.10
    wrapper = 50

class quarter(coin):
    weight = 5.670
    value = 0.25
    wrapper = 40

class half(coin):
    weight = 11.340
    value = 0.50
    wrapper = 20

class dollar(coin):
    weight = 8.1
    value = 1.00
    wrapper = 20

def user_input():
    """
    takes users input of: coin type, total weight
    returns: number of wrappers the user needs
             how many coins the user has
             estimated total value of coins
    """
    
    #print coin.cointype
    
    # bl flag for repeat coin entry
    user_has_coins = 1

    # take user input
    while user_has_coins:
        user_coin = raw_input("Please enter your coin type: ")
        user_weight = raw_input("Please enter coins total weight: ")
        user_choice = raw_input("Do you have more coins to enter(Y/N): ")
        user_choice = user_choice.upper()
        if user_choice == "N":
            user_has_coins = 0

    # calculate values for user input
    num_coins = user_weight / user_coin.weight
    num_coins = int(num_coins)
    num_wrappers = num_coins / usercoin.wrapper
    # need to round up
    num_wrappers = round(num_wrappers)
    est_value = num_coins * round(user_coin.value, 2)
    # output user results
    return num_wrappers, num_coins, est_value

#user_input()
