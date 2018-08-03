def main():
    user_data = input('Enter a string: ')
    user_data = user_data.upper()
    number_characters = len(user_data)
    letters = []
    for i in range(number_characters):
        if user_data[i].isalpha():
            if user_data[i] not in letters:
                letters.append(user_data[i])
    letter_count = []
    letters_to_count = len(letters)
    for i in range(letters_to_count):
        letter_count.append(user_data.count(letters[i]))
    for i in range(len(letters)):
        print(str(letters[i]) + " " + str(letter_count[i]))


main()
