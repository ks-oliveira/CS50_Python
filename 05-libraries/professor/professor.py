import random

def main():
    level = get_level()
    errors = 0
    totalErrors = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer == (x + y):
                    break
                else:
                    raise ValueError

            except ValueError:
                errors += 1
                if errors < 3:
                    print("EEE")
                    pass
                else:
                    print("EEE")
                    totalErrors += 1
                    print((f"{x} + {y} = {x + y}"))
                    break

    print(f"Score: {10 - totalErrors}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <=3:
                return level
        except:
            pass


def generate_integer(level):

    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()