def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    size = len(s)

    if size < 2 or size > 6:
        return False

    for i in range(2):
        if (s[i].isalpha() != True):
            return False

    for i in range(size):
        if i < size - 1:
            j = i + 1

        if s[i].isalnum() != True:
            return False

        # Verify if after the number has a letter
        if s[i].isnumeric() and s[j].isalpha():
            return False


    # Verify if the first number is zero
    count = 1
    while s[count].isnumeric() != True and count < size - 1:
        if s[count + 1] == '0':
            return False
        count += 1

    return True

main()