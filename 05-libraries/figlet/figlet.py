import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font" or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))