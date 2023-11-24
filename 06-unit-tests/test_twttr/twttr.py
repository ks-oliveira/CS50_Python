def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    str = ""
    for char in word:
        if (char.lower() not in "aeiou"):
            str += char

    return str


if __name__ == "__main__":
    main()