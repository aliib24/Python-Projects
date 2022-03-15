
from tkinter.ttk import LabeledScale

from termcolor import colored

kg = float(input("Please enter the KG: "))

lbs = float(2.2046 * kg)

print("The lbs is: \n")

print(colored(lbs , 'yellow'))
