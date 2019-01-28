### Doesn't work
##def fib(num):
##    a = 0
##    b = 1
##    for i in xrange(num):
##        a = b
##        b = a + b
##        print a

def fibonacci(number):
    a,b = 0,1
    print a
    for i in xrange(number):
        a, b = b, a + b
        print a

#fibonacci(100)

##def fib_rec(num):
##    if num == 0:
##        return num
##    elif num == 1:
##        return num
##    else:
##        fib_rec(num - 1 + num - 2)
