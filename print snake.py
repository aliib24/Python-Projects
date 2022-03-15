
snake = int(input("Please enter the number to draw the snake: "))

for i in range (snake):

    if snake % 2 == 0:
        print("🟩" , end="")

    else:
        print("🟨" , end="")

    snake = snake - 1
