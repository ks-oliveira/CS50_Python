while True:
    try:
        numerator, denominator = input("Fraction: ").split('/')
        numerator = int(numerator)
        denominator = int(denominator)

        fuel = round(numerator / denominator * 100)

        if fuel < 0 or fuel > 100:
            fuel = fuel / 0
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break


if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print(f"{fuel}%")