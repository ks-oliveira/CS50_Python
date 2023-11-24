def main():
    greetings = input("Greeting: ")
    print(f"${value(greetings)}")

def value(greeting):
    greeting = greeting.strip()
    greeting = str.lower(greeting)

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()