import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    args_verification(sys.argv)

    try:
        image = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size

    photo = ImageOps.fit(image, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2], format=None)


def args_verification(arguments):
    formats = [".jpg", ".jpeg", ".png"]
    commands = len(arguments)
    if commands < 3:
        sys.exit("Too few command-line arguments")
    if commands > 3:
        sys.exit("Too many command-line arguments")


    file1 = os.path.splitext(arguments[1].lower())[1]
    file2 = os.path.splitext(arguments[2].lower())[1]


    if isFileValid(file1, formats) == False:
        sys.exit("Invalid input")
    if isFileValid(file2, formats) == False:
        sys.exit("Invalid output")
    if isSameFormat(file1, file2, formats) == False:
        sys.exit("Input and output have different extensions")

def isFileValid(str, arr):
    for format in arr:
        if format == str:
            return True

    return False

def isSameFormat(str1, str2, arr):
    for format in arr:
        if format == str1 and format == str2:
            return True

    return False


if __name__ == "__main__":
    main()