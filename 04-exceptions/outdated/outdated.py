months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    try:
        date = input("Date: ")
        if date.find("/") > -1:
            month, day, year = date.split('/')
            if month in months:
                value = 1 / 0

        elif date.find(",") > -1:
            i, year = date.split(', ')
            month, day = i.split()
            if month in months:
                month = months[month]
            else:
                value = 1 / 0
                
        else:
            value = 1 / 0

        year = int(year)
        month = int(month)
        day = int(day)

        if month < 1 or month > 12 or day < 1 or day > 31:
            value = 1 / 0

    except ZeroDivisionError:
        pass
    else:
        break

print(f"{year:04}-{month:02}-{day:02}")