import string

lowercase_alphabet = list(string.ascii_lowercase)
user_message = input("Type your message: ")
user_key = int(input('type a number: '))
coded_message = ""

user_message_list = list(user_message)

for word in user_message_list:
    if word.isalpha():
        for letter in word:
            for index, alphabet in enumerate(lowercase_alphabet):
                if letter == alphabet:
                    new_index = index + user_key
                    if new_index > 25:
                        new_index = new_index % 25
                        coded_message += lowercase_alphabet[new_index]
                    else:
                        coded_message += lowercase_alphabet[new_index]
    elif word == " ":
        coded_message += " "

print(coded_message)




