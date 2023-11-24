import validators


def main():
    print(validation(input("Text: ")))


def validation(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()