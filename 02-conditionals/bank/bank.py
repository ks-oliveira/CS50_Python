greetings = input("Greeting: ")
greetings = greetings.strip()
greetings = str.lower(greetings)

if greetings.startswith("hello"):
    print("$0")
elif greetings.startswith("h"):
    print("$20")
else:
    print("$100")