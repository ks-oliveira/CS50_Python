def main():
    text = input()
    print(convert(text))


def convert(text):
    faced_smile = ':)' in text
    faced_sad = ':(' in text

    if(faced_smile or faced_sad):
        text = text.replace(':)', '🙂')
        text = text.replace(':(', '🙁')

    return text


main()