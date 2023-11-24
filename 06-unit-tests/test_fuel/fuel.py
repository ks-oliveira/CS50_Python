def main():
    while True:
        try:
            n = input("Fraction: ")
            fuel = convert(n)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    print(gauge(fuel))


def convert(fraction):
    numerator, denominator = fraction.split('/')
    numerator = int(numerator)
    denominator = int(denominator)

    if denominator == 0:
        raise ZeroDivisionError

    percentage = round(numerator / denominator * 100)

    if percentage < 0 or percentage > 100:
        raise ValueError
    else:
        return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()