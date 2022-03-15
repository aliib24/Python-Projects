from contextlib import redirect_stderr
from termcolor import colored

les1 = input("please enter the name of the lesson: ")
mk1 = float(input("please enter the mark of student: "))

les2 = input("please enter the name of the lesson: ")
mk2 = float(input("please enter the mark of student: "))

les3 = input("please enter the name of the lesson: ")
mk3 = float(input("please enter the mark of student: "))

avg = float((mk1 + mk2 + mk3) / 3)

print("Students Average is: ")

print(colored(les1 , 'yellow'))
print(colored(mk1 , 'blue'))

print(colored(les2 , 'yellow'))
print(colored(mk2 , 'blue'))

print(colored(les3 , 'yellow'))
print(colored(mk3 , 'blue'))

print( colored("Average: " + str(avg) + "\n" , "red"))






