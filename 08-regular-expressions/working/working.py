import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s):
        first_hour = time(matches.group(2), matches.group(3), matches.group(4))
        second_hour = time(matches.group(6), matches.group(7), matches.group(8))

        return f"{first_hour} to {second_hour}"
    else:
        raise ValueError

def time(hour, minutes, type):
    hour = int(hour)

    if minutes != None:
        minutes = int(minutes)
    else:
        minutes = 0

    if minutes > 59:
        raise ValueError

    if type == "PM" and hour < 12:
        hour += 12
    elif type == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minutes:02}"

if __name__ == "__main__":
    main()