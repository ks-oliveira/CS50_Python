groceries = {}
listSorted = {}

while True:
    try:
        item = str.upper(input())

        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] += 1

    except EOFError:
        if len(groceries) > 0:
            keys = list(groceries.keys())
            keys.sort()
            for i in keys:
                listSorted[i] = groceries[i]

            for i in listSorted:
                print(f"{listSorted[i]} {i}")

        break