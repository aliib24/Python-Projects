from termcolor import colored

# ax + b = 0

a = float(input("please enter the a "))

b = float(input("please enter the b "))

x = float( -b / a )

print("the answer is: ")
print(colored( x , 'blue'))