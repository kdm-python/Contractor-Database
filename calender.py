import calendar
import datetime

###########################
### CONTRACTOR DATABASE ###
###########################

# CALENDER MODULE

def test1():
    # importing the calendar module
    # initializing the year
    year = 2019
    # printing the calendar
    print(calendar.calendar(2019))

def test2():
    # initializing the year and month number
    year = 2000
    month = 1
    # getting the calendar of the month
    print(calendar.month(year, month))

test2()