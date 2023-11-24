import csv
from tabulate import tabulate
import sys

def main():
    args_verification(sys.argv, "csv")
    table = []

    try:
        with open(sys.argv[1], newline='') as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                table.append(row)

            header = table[0]
            print(tabulate(table[1:], header, tablefmt="grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")


def args_verification(arguments, file_tipe):
    commands = len(arguments)
    len_file_type = len(file_tipe) + 2

    if commands < 2:
        sys.exit("Too few command-line arguments")
    if commands > 2:
        sys.exit("Too many command-line arguments")

    length = len(arguments[1])

    if sys.argv[1].find(".csv", (length - len_file_type)) == -1:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()