import random as rnd
from sys import flags
from termcolor import colored as cl

inplst = []

xi = int(input(cl("Please enter the lenght of array: " , 'green')))

rndl = int(input(cl("Please enter the lenght of randomizer: " , 'green')))

for i in range(0 , xi):

    buff = int(rnd.randint(1 , rndl))
    inplst.append(buff)

print(cl(inplst , 'yellow'))

