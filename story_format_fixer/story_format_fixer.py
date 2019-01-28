# t 30 m
# would be more efficient to use and write directly
# urllib.retrieve(url[, filename[, reporthook[, data]]])
# or to parse the story first and write to a file once

# get our story from online text
import urllib
story = urllib.urlopen(https://pastebin.com/raw/XMY48CnN)


# create a file
file = open("greeneggsham.txt", "w+")

# copy story into a text file
with open("greeneggsham.txt", "a" as the_file:
          the_file.write(story)

# read the story
story = greeneggsham.txt.read()

newstory = ""
num_error = 0

# make the "i" uppercase
for character in story:
    if character == "i":
          num_error += 1
          character = character.upper()
          newstory += character

# create a new file
file = open("greeneggsham_fix.txt", "w+")

# write the appended story to the file
with open("greeneggsham_fix.txt", "a" as the_file:
          the_file.write(story)

# print out the number of errors
print "Number of errors: ", num_error
