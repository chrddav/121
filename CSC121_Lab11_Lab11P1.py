user_input = input('Enter a string: ').upper()
string_length = len(user_input)
characters = []
for i in range(string_length):
    if user_input[i].isalpha():
        if user_input[i] not in characters:
            characters.append(user_input[i])
char_count = []
for i in range(len(characters)):
    char_count.append(user_input.count(characters[i]))
combined = list(zip(characters, char_count))
dictionary = dict(combined)

user_char = input('Choose a letter: ')
user_char = user_char.upper()
if user_char in dictionary:
    print('Frequency count of that letter: ', dictionary[user_char])
    del dictionary[user_char]
else:
    print('Letter not in dictionary.')
print('Dictionary after that letter removed: ', dictionary)

letters = dictionary.keys()
sorted_char = sorted(letters)
print('Letters sorted: ', sorted_char)
