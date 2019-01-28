# beer song
# 15m

# initialize variables
num_bottles = 99
words = "bottles of beer"
words2 = "Take one down and pass it around,"
words3 = "on the wall."

# until we have 2 bottles
while num_bottles > 2:
    # sing the song and remove 1 bottle
    for i in range(0, 97):
        print "%s %s %s" % (num_bottles, words, words3)
        print "%s %s." % (num_bottles, words)
        print words2
        num_bottles -= 1
        print "%s %s %s \n" % (num_bottles, words, words3)
        
# 2 bottles left
print "%s %s %s" % (num_bottles, words, words3)
print "%s %s." % (num_bottles, words)
print words2
num_bottles -= 1
print "%s bottle of beer %s \n" % (num_bottles, words3)

# 1 bottle left
print "%s bottle of beer %s" % (num_bottles, words3)
print num_bottles, "bottle of beer." 
print words2
num_bottles -= 1

# ran out of beer
print "No more %s %s \n" % (words, words3)
print "No more %s %s" % (words, words3)
print "No more", words
print "Go to the store and buy some more, \nNo more %s %s" % (words, words3)
