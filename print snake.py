from numpy import intp

snake = int(input("Please enter the number to draw the snake: "))

while snake > 0:

    if snake % 2 == 0:
        print("🟩" , end="")

    else:
        print("🟨" , end="")

    snake = snake - 1