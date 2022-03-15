import datetime
from termcolor import colored
from re import S

s = int(input("Please eneter the Seconds: "))

h = str(datetime.timedelta( seconds= s))

print(colored(h , 'yellow'))