import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        for matche in matches.groups():
            matche = int(matche)
            print(matche)
            if matche < 0 or matche > 255:
                return False
        return True

    return False


if __name__ == "__main__":
    main()