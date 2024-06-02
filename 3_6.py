def generate_acronym(sentence):
    words = sentence.split() 
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

user_input = input("Enter the string: ")

acronym = generate_acronym(user_input)
print(f"Abbreviation: {acronym}")
