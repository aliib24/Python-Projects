from numpy import insert, sort
from termcolor import colored

inplst = []

flag = 0

xi = int(input("Please enter the lenght of LIST"))

for i in range (0,xi):

    le = int(input())
    inplst.append(le)

    test_list = inplst[:]
    test_list.sort()

if (inplst == sorted(inplst)):
    flag = 1

if (flag):
    print(colored("The list is sorted." , 'yellow'))
    print(colored(inplst , 'blue'))

else:
    print(colored("The list is not sorted." , 'yellow'))
    print(colored(inplst , 'blue'))