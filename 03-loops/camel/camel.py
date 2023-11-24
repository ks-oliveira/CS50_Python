camel = input("camelCase: ")
print("snake_case: ", end="")

for char in camel:
    if char.isupper():
        print("_", end="")
        char = str.lower(char)
    print(char, end="")

print()
