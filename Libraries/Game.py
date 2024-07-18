from random import randint
import sys

if len(sys.argv) == 1:
    while True:
        try:
            random_number = randint(1, int(input("Level: ")))
            if random_number > 0:
                break
        except ValueError:
            "An error occured"

elif len(sys.argv) == 2:
    random_number = randint(1, int(sys.argv[1]))
else:
    sys.exit("Too many arguments")

while True:
    try:
        guess = int(input("Guess: "))
        if guess < random_number:
            print("Too small")
        elif guess > random_number:
            print("Too big")
        else:
            print("Just right!")
            break
    except ValueError:
        "An error occured"
