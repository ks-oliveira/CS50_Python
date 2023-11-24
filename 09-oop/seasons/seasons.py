from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalide Date")

    date_of_birth = date(year, month, day)
    today = date.today()

    count_days = (today - date_of_birth).days
    count_minutes = count_days * 24 * 60
    text_minutes = p.number_to_words(count_minutes, andword="")

    print(f"{text_minutes.capitalize()} minutes")

def check_birthday(date):
    if date := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", date):
        year = int(date.group(1))
        month = int(date.group(2))
        day = int(date.group(3))
        return year, month, day


if __name__ == "__main__":
    main()
