from termcolor import colored

from termcolor import colored

h = int(input("Please enter the H parameter: "))
m = int(input("Please enter the M parameter: "))
s = int(input("Please enter the S parameter: "))

if m > 60:

    print("minute is more than 60 minutes")

elif s > 60:

    print("Second is more than 60 seconds")

else:

    seconds = h * (3600) + m * (60) + s
    print(colored(seconds , 'yellow'))
