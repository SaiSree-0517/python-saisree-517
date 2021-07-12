"""
Python datetime
Python has a module named datetime to work with dates and times.
"""
#Example 1: Get Current Date and Time
import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)
"""
output
2021-07-12 10:17:13.449928
"""

"""
Here, we have imported datetime module using import datetime statement.
One of the classes defined in the datetime module is datetime class. We then used now()
method to create a datetime object containing the current local date and time.
"""
#Example 2: Get Current Date
import datetime
date_object = datetime.date.today()
print(date_object)
"""
output:
2021-07-12
"""
"""
In this program, we have used today() method defined in the date class to get a
date object containing the current local date.
"""
#We can use dir() function to get a list containing all attributes of a module.
import datetime
print(dir(datetime))
"""
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
'__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime',
'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""

"""
Commonly used classes in the datetime module are:

1.date Class
2.time Class
3.datetime Class
4.timedelta Class
"""

"""
datetime.date Class
You can instantiate date objects from the date class.
A date object represents a date (year, month and day).
"""
#Example 3: Date object to represent a date
import datetime
d = datetime.date(2021, 7, 11)
print(d)
"""
output
2021-07-11
"""
"""
If you are wondering, date() in the above example is a constructor of the date class.
The constructor takes three arguments: year, month and day.
"""

#We can only import date class from the datetime module. 
from datetime import date
a = date(2021, 7, 11)#The variable a is a date object.
print(a)
"""
output
2021-07-11
"""

"""
Example 4: Get current date
You can create a date object containing the current date by using a classmethod named today().
"""
from datetime import date
today = date.today()
print("Current date =", today)#Current date = 2021-07-12


"""
Example 5: Get date from a timestamp
We can also create date objects from a timestamp.
A Unix timestamp is the number of seconds
between a particular date and January 1, 1970 at UTC.
You can convert a timestamp to date using fromtimestamp() method.
"""

from datetime import date
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)#Date = 2012-01-11

"""
Example 6: Print today's year, month and day
We can get year, month, day, day of the week etc. from the date object easily
"""
from datetime import date
# date object of today's date
today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
"""
Current year: 2021
Current month: 7
Current day: 12
"""

"""
datetime.time
A time object instantiated from the time class represents the local time.

Example 7: Time object to represent time
"""

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)
# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)
"""
a = 00:00:00
b = 11:34:56
c = 11:34:56
d = 11:34:56.234566
"""

"""
Example 8: Print hour, minute, second and microsecond
Once you create a time object, you can easily print its attributes such as hour, minute etc.
"""

from datetime import time
a = time(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)
"""
hour = 11
minute = 34
second = 56
microsecond = 0
"""


"""
datetime.timedelta
A timedelta object represents the difference between two dates or times.

Example 9: Difference between two dates and times
"""
from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))
"""
t3 = 201 days, 0:00:00
t6 = -333 days, 1:14:20
type of t3 = <class 'datetime.timedelta'>
type of t6 = <class 'datetime.timedelta'>
"""

#Example 10: Difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)#t3 = 14 days, 13:55:39

"""
Example 11: Time duration in seconds
You can get the total number of seconds in a timedelta object using total_seconds() method.
"""

from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())#total seconds = 435633.233423



"""
Python format datetime
The way date and time is represented may be different in different places, organizations etc.
It's more common to use mm/dd/yyyy in the US, whereas dd/mm/yyyy is more common in the UK.

Python has strftime() and strptime() methods to handle this.

Python strftime() - datetime object to string
The strftime() method is defined under classes date, datetime and time.
The method creates a formatted string from a given date, datetime or time object.
"""

#Example 12: Format date using strftime()
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)
"""
time: 13:51:17
s1: 07/12/2021, 13:51:17
s2: 12/07/2021, 13:51:17
"""

"""
Here, %Y, %m, %d, %H etc. are format codes.
The strftime() method takes one or more format codes and returns a formatted string based on it.

In the above program, t, s1 and s2 are strings.

%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - minute [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 59]
"""


"""
Python strptime() - string to datetime
The strptime() method creates a datetime object from a given string (representing date and time).
"""
#Example 13: strptime()

from datetime import datetime

date_string = "25 November, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
"""
date_string = 25 November, 2018
date_object = 2018-11-25 00:00:00
"""

"""
The strptime() method takes two arguments:

a string representing date and time
format code equivalent to the first argument
By the way, %d, %B and %Y format codes are used for day, month(full name) and year respectively.
"""



