import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"(.+?)\"", s):
        if embURL := re.search(r"youtube.com/embed/(.+)", matches.group(1)):
            return f"https://youtu.be/{embURL.group(1)}"

    return "None"

if __name__ == "__main__":
    main()