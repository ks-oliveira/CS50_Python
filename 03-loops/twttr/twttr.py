def main():
    text = input("Input: ")

    for char in text:
        if (isVowel(char) != True):
            print(char, end="")

    print()


def isVowel(c):
    c = c.lower()

    for vowel in "aeiou":
        if c == vowel:
               return True

    return False

main()