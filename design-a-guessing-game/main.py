# import random module
import random

correct_guess = False
random_number = random.randrange(1,100)

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")
    try:
        number = int(user_input)
        if random_number == number:
            correct_guess = True
        elif number > random_number:
            print("You guessed too high")
        elif number < random_number:
            print("You guessed too low")
    except:
        print("Enter a NUMBER")



print("You guessed the right number!")

