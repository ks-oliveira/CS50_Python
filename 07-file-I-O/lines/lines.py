import sys

def main():
    commands = len(sys.argv)
    LoC = 0

    if commands < 2:
        sys.exit("Too few command-line arguments")
    if commands > 2:
        sys.exit("Too many command-line arguments")

    length = len(sys.argv[1])

    if sys.argv[1].find(".py", (length - 4)) == -1:
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()

            for line in lines:
                if isComment(line) == False:
                    LoC += 1

            print(LoC)

        except FileNotFoundError:
            sys.exit("File does not exist")

def isComment(string):
    string = string.strip(" ")
    if string.startswith("#") or string.isspace():
        return True
    else:
        return False


if __name__ == "__main__":
    main()