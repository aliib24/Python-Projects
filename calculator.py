from math import fabs
from random import choices
from re import I
from tkinter import N
from termcolor import colored
import math
from math import cos,sin


# Classes

def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    return x / y

def tanjent(x):
    return math.tan(x)

def cotanjent(x , y):
    return(cos(x) / sin(y))

# The Menu
print("Select operation")
print(colored("1. Add" , 'blue'))
print(colored("2. Subtract" , 'blue'))
print(colored("3. Mulitply" , 'blue'))
print(colored("4. Divide", 'blue'))
print(colored("5. Factorial" , 'blue'))
print(colored("6. Tanjent" , 'blue'))
print(colored("7. Cotanjent" , 'blue'))
print(colored("0. exit" , 'yellow'))

# Restart statement
while True:

    choice = input("Enter choice(1/2/3/4/5/6/7/0): ")

    if choice in ('1','2','3','4','5','6','7','0'):
        
        if choice == '1':
            num1 = float(input("Enter the fist number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 , "+" , num2 , "=" , add(num1 , num2))

        elif choice == '2':
            num1 = float(input("Enter the fist number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 , "-" , num2 , "=" , subtract(num1 , num2))
        
        elif choice == '3':
            num1 = float(input("Enter the fist number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 , "x" , num2 , "=" , multiply(num1 , num2))
        
        elif choice == '4':
            num1 = float(input("Enter the fist number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 , "/" , num2 , "=" , divide(num1 , num2))

        elif choice == '5':
            x = int(input("please enter the number: "))
            fact = int(input("please enter the factorial number: "))
            for i in range(1 , x + 1):
                fact = fact * i
            print("The factorial of" ,x, "is: ",end=" ")
            print(colored(fact , 'yellow'))

        elif choice == '6':
            num = int(input("Enter6 degree: "))
            print("Tanjent of" , num , "is: ", tanjent(num))

        elif choice == '7':
            num1 = int(input("Enter cosinus: "))
            num2 = int(input("Enter sinus: "))
            print("The cotangent is",cotanjent(num1 , num2))

        next_calculation = input("Do you want to continue ? (y/n): ")
        if next_calculation == "n":
            break
        
    else:
        print("Invalid input")
