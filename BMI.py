from termcolor import colored

print("BMI \n")

w = float(input("Please enter your weight(kg): "))

h = float(input("Please enter you height(m): "))

h2 = pow(h , 2)

bmi = w / h2

print(bmi)