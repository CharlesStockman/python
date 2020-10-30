# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
# from datetime import date, time, datetime
# some_date = date(2002, 2, 22)
# some_time = time(9, 45, 23)
# one_from_two(some_date, some_time) => datetime object representing 
# 2002-02-22 09:45:23

from datetime import date, time, datetime

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)


def algorithm(some_date:date, some_time:time) -> datetime:
    def one_from_two(some_date:date, some_time:time) -> datetime:
        value = datetime( some_date.year, some_date.month, some_date.day, some_time.hour, some_time.minute, some_time.second)
        return value
    print("The combination of date and time is ", one_from_two(some_date, some_time))

algorithm(some_date, some_time)
