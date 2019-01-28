#t 30m
# welcome message
print "Welcome to mad-libs generator"

# user word input
familymember = raw_input("Please enter a family member role, e.g, uncle: ")
adjective = raw_input("Please enter an adjective to describe them, e.g, wild: ")
verb1 = raw_input("Please enter an activity they would do: ")
verb2 = raw_input("Please enter another similar activity they would do: ")
word = raw_input("Please enter a fictional name for a trophy: ")

# capitalize the trophy title
wordlist = word.split()
newword = ""
for words in wordlist:
    newword += words[0].upper() + words[1: ] + " "

    
# use correct grammar for vowels
vowel_word = ""
if familymember[0] in "aeiou":
    vowel_word = "an"
else:
    vowel_word = "a"

print "Generating story..."
# ouput
print "I had %s %s who was %s.\nEvery day they would go %s." % (vowel_word, familymember, adjective, verb1)
print "Eventually they decided to go %s. \nand they ended up winning the %s" % (verb2, newword)
print "What a great %s." % familymember
