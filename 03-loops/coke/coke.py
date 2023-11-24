sum = 50

while sum > 0:
    print(f"Amount Due: {sum}")
    value = int(input("Insert Coin: "))

    match value:
        case 25:
            sum -= value
        case 10:
            sum -= value
        case 5:
            sum -= value

sum = -1 * sum
print(f"Change Owed: {sum}")