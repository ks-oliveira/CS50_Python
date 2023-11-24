def main():
    time = input("What time is it? ")
    # time = time.strip()
    # time = str.lower(time)

    # check if it is a.m. or p.m.
    time = timeFormat(time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    return hours + minutes / 60

def timeFormat(time):
    if time.endswith("p.m.") or time.endswith("a.m."):
        time, format = time.split(" ")

        if format == "p.m.":
            return convert(time) + 12
        else:
            return convert(time)
    else:
        return convert(time)

if __name__ == "__main__":
    main()