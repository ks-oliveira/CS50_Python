import csv
from tabulate import tabulate
from colorama import Fore, init
init()

color = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW,
    'reset': Fore.RESET,
}

def main():
    filecsv = "kanban.csv"
    try:
        table = open_file(filecsv)
    except FileNotFoundError:
        table = []

    write_file(table)

    while True:
        show_table(kanban())

        print(f"{color['green']} \nKanban Actions {color['reset']}")

        option = action()

        if option in ["I","M","U","D"]:
            table = open_file(filecsv)

        if option == "I":
            item = input(f"{color['blue']}What is the new To Do?{color['reset']} ")
            write_file(insert_item(table, item))

        elif option == "M":
            # Choose the item to be moved
            run = True
            while run:
                item = input(f"{color['blue']}Which item do you want to move?{color['reset']} ")
                item, run = value(item, range(1,len(table)))

            # Choose what will be the new status
            status_list = [['Status number', 'status'],['1', 'To Do'], ['2', 'Doing'], ['3', 'Done']]
            run = True
            while run:
                print(f"{color['blue']}What is the the status for the item {item} (choose a status number)?{color['reset']}")
                print(tabulate(status_list[1:], status_list[0], tablefmt="rounded_grid"))
                status = input("1, 2 or 3? ")
                status, run = value(status, range(1,4))

            status = status_list[int(status)][1]
            write_file(update_item(table, option, item, status))

        elif option == "U":
            # Choose the item to be renamed
            run = True
            while run:
                item = input(f"{color['blue']}Which item do you want to rename?{color['reset']} ")
                item, run = value(item, range(1,len(table)))

            newname = input(f"{color['blue']}What is the new name of the item?{color['reset']} ")
            write_file(update_item(table, option, item, newname))

        elif option == "D":
            # Choose the item to be removed
            run = True
            while run:
                item = input(f"{color['blue']}Which item do you want to remove?{color['reset']} ")
                item, run = value(item, range(1,len(table)))


            write_file(delete_item(table, item))

        elif option == "E":
            break

# What are the actions to do in kanban table
def action():
    table = [
        [f"{color['blue']}Key{color['reset']} ",f"{color['blue']}Action{color['reset']} "],
        ['I','Include Item'],
        ['M','Move Item'],
        ['D','Delete Item'],
        ['U','Update Item'],
        ['E','Exit']
    ]

    show_table(table)
    option = input(f"{color['blue']}What do you want to do:{color['reset']} ")

    return option.upper()

# Create the kanban table
def kanban():
    print(f"{color['green']} \nThis is your Kanban {color['reset']}")
    table = []
    table.append([f"{color['red']}To Do{color['reset']}", f"{color['yellow']}Doing{color['reset']}", f"{color['green']}Done{color['reset']}"])

    with open("kanban.csv", newline='') as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            if row[1] == "To Do":
                table.append([f"{row[0]} - {row[2]}","",""])
            if row[1] == "Doing":
                table.append(["",f"{row[0]} - {row[2]}",""])
            if row[1] == "Done":
                table.append(["","",f"{row[0]} - {row[2]}"])

    return table

def insert_item(table, item):
    line = [f"{len(table)}", "To Do", item]
    table.append(line)
    return table

def delete_item(table, item):
    newtable = []
    newtable.append(table[0])

    for row in table[1:]:
        if row[0] != str(item):
            newtable.append([f"{len(newtable)}", row[1], row[2]])

    return newtable

def update_item(table, option, item, info):
    item_line = table[item]

    if option == "U":
        table[item] = [item_line[0], item_line[1], info]

    if option == "M":
        table[item] = [item_line[0], info, item_line[2]]

    return table

# Open csv file
def open_file(file):
    table = []
    with open(file, newline='') as oldfile:
        oldcsvfile = csv.reader(oldfile)
        for row in oldcsvfile:
            table.append(row)

    return table

# Write in csv file
def write_file(data):
    table = data
    header = ["ID","Status","Item"]

    with open("kanban.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow({header[0]: header[0], header[1]: header[1], header[2]: header[2]})

        for row in table[1:]:
            writer.writerow({header[0]:row[0], header[1]:row[1], header[2]:row[2]})


def show_table(table):
    header = table[0]
    print(tabulate(table[1:], header, tablefmt="rounded_grid"))

# Evaluate the values given by input
def value(item, rang):
    run = True
    invalid = False

    if item.isdigit():
        item = int(item)

        if item in rang:
            run = False
        else:
            invalid = True
    else:
        invalid = True

    if invalid:
        print(f"{color['red']}!!! Invalid Key !!!{color['reset']}")

    return item, run


if __name__ == "__main__":
    main()
