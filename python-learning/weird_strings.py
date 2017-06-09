string = "Weird string case"
string_processed = []

for word in string.split(" "):
    word_processed = ""
    even = True
    for character in word:
        word_processed = word_processed + (character.upper() if even else character.lower())
        even = False if even else True 
    string_processed.append(word_processed)

print " ".join(string_processed)