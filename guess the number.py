import random
from termcolor import colored

# Main Menu

print("Select the difficuly of game")
print(colored("1. super easy" , 'blue'))
print(colored("2. easy" , 'blue'))
print(colored("3. noraml" , 'blue'))
print(colored("4. hard", 'blue'))
print(colored("5. super hard" , 'blue'))
print(colored("6. insane!!!" , 'blue'))
print(colored("0. exit" , 'yellow'))

while True:
    
    choice = input("Enter choice(1/2/3/4/5/6/0)")


    if choice in ('1','2','3','4','5','6','0'):

        if choice == '1':
            counter = 0
            
            while counter < 20:
                print("Super Easy \n")
                x = int(input("Enter your guess: "))
                n = random.randint(1 , 10)
                if x < n:
                    print("guess is low")
                    counter += 1
                elif x > n:
                    print("guess is high")
                    counter +=1
                else:
                    print("you guessed it...")
                    print(counter)

        if choice == '2':
            counter = 0 
            while counter < 10:
                print("Easy \n")
                x = int(input("Enter your guess: "))
                n = random.randint(1 , 20)
                if x < n:
                    print("guess is low")
                    counter += 1
                elif x > n:
                    print("guess is high")
                    counter +=1
                else:
                    print("you guessed it...")
                    print(counter)

        elif choice == '3':
            counter = 0
            while counter < 5:
                print("Normal \n")
                x = int(input("Enter your guess: "))
                n = random.randint(1 , 50)
                if x < n:
                    print("guess is low")
                    counter += 1
                elif x > n:
                    print("guess is high")
                    counter +=1
                else:
                    print("you guessed it...")
                    print(counter)

        elif choice == '4':
            counter = 0
            while counter < 3:
                print("Hard \n")
                x = int(input("Enter your guess: "))
                n = random.randint(1 , 70)
                if x < n:
                    print("guess is low")
                    counter += 1
                elif x > n:
                    print("guess is high")
                    counter +=1
                else:
                    print("you guessed it...")
                    print(counter)

        elif choice == '5':
            counter = 0
            while counter < 2:
                print("Super Hard \n")
                x = int(input("Enter your guess: "))
                n = random.randint(1 , 100)
                if x < n:
                    print("guess is low")
                    counter += 1
                elif x > n:
                    print("guess is high")
                    counter +=1
                else:
                    print("you guessed it...")
                    print(counter)

        elif choice == '1':
            counter = 0
            while counter < 1:
                print("Insane \n")
                x = int(input("Enter your guess: "))
                n = random.randint(1 , 200)
                if x < n:
                    print("guess is low")
                    counter += 1
                elif x > n:
                    print("guess is high")
                    counter +=1
                else:
                    print("you guessed it...")
                    print(counter)
        
        else:
            print("Invalid Input")