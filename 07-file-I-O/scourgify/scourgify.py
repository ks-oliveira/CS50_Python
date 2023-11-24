import csv
import sys

def main():
    args_verification(sys.argv)
    table = []

    try:
        with open(sys.argv[1], newline='') as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                table.append(row)

        with open(sys.argv[2], 'w', newline='') as newfile:
            header = ["first", "last", "house"]
            writer = csv.DictWriter(newfile, fieldnames=header)
            writer.writerow({header[0]: header[0], header[1]: header[1], header[2]: header[2]})

            for row in table[1:]:
                last_name, first_name = row[0].split(",")
                first_name = first_name.strip()
                house = row[1]
                writer.writerow({header[0]: first_name, header[1]: last_name, header[2]: house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def args_verification(arguments):
    commands = len(arguments)

    if commands < 3:
        sys.exit("Too few command-line arguments")
    if commands > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()