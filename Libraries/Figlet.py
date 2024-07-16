from pyfiglet import Figlet
import sys
import random


if len(sys.argv) == 1:  # 0 arguments
    ...
elif len(sys.argv) == 3: # 2 arguments
    ...
elif len(sys.argv) == 2:
    sys.exit("Please enter 0 or 2 arguments")
else:
    sys.exit("Too many arguments")

message = input("Your message: ")
