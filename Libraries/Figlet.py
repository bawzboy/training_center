from pyfiglet import Figlet
import sys
from random import randint

figlet = Figlet()
list_of_fonts = figlet.getFonts() # 549 fonts

if len(sys.argv) == 1:  # = 0 arguments
    random_font = randint(0, len(list_of_fonts))
    figlet.setFont(font = list_of_fonts[random_font])
elif len(sys.argv) == 3:  # = 2 arguments
    if sys.argv[1] == "-f" or "--font":
        figlet.setFont(font = sys.argv[2])
elif len(sys.argv) == 2:
    sys.exit("Please enter 0 or 2 arguments")
else:
    sys.exit("Too many arguments")

message = input("Your message: ")
print(figlet.renderText(message))
