import random


running = True
while running:
    try:
        min, max = int(input("Input the minimum and maximum numbers for the game. \nMinimum: ")), int(input("Maximum: "))
        num = random.randint(min, max)
        #print(num)
    except Exception as e:
        print("Invalid input please try again. Input the minimum and maximum of the range you  would like to guess on.")

    correct = False
    while not correct:
        guess = int(input("What is your guess? "))
        if guess > num:
            print("Guess lower!")
        elif guess < num:
            print("Guess higher!")
        else: 
            print("Correct!")
            correct = True
            

            

    while correct:
        again = input("Would you like to play again? (y/n)")
        if again == "y":
            print("Restarting")
            correct = False
        elif again == "n":
            print("C ya!")
            running = False
            correct = False
        else:
            print("Not a valid answer")

