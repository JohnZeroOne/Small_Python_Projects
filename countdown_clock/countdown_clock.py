# there is probably a much more efficient way to do this
#import sys
import time

print "Welcome to countdown clock"
print "You can enter a date and time and I will tell you how much longer there is to wait"
print "\nThe current date and time are:", time.asctime()
# get the current time and date
current_time = time.asctime()
# slice it into variables
day_name = current_time[0:3]
month = current_time[4:7]
day = current_time[8:10]
hour = current_time[11:13]
minute = current_time[14:16]
second = current_time[17:19]
year = current_time[20:]
# test formatting
#print "day %s month %s day %s hour %s minute %s second %s year %s" % (day_name, month, day, hour, minute, second, year)

# time interval seconds
num_sec = 0
# get user date-time
user_entry = raw_input("\nPlease enter a time and date, format (dd/mm/yy:hh/mm/ss): ")
# slice user input into variables
user_date = user_entry[0:2]
print "date:", user_date
user_month = user_entry[3:5]
print "month:", user_month
user_year = user_entry[6:8]
print "year:", user_year
user_hour = user_entry[9:11]
print "hour:", user_hour
user_mins = user_entry[12:14]
print "mins:", user_mins
user_secs = user_entry[15:]
print "secs:", user_secs
# test formatting
print "date %s month %s hour %s minute %s second %s year %s" % (user_date, user_month, user_hour, user_mins, user_secs, user_year)


# compare user date against current time

while True:
    time.sleep(1)
    num_sec += 1
    print "It has been %s seconds" % num_sec
