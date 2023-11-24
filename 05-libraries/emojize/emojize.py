import emoji

text = input("Input: ")
text = emoji.emojize(text, language='alias')

print(f"Output: {text}")