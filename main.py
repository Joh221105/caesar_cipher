import string

# creates a list of lower case alphabet a-z
lowercase_alphabet = list(string.ascii_lowercase)

# get user input for the message and the key for encoding
user_message = input("Type your message: ").lower()
user_key = int(input('Type a number: '))

# accounts for both positive and negative keys
user_key = user_key % 26

# Convert the user message to a list of words
user_message_list = list(user_message)

def encode(user_message_list, user_key):
    coded_message = ""
    for letter in user_message_list:
        if letter.isalpha():
            # Find the index of the letter in the alphabet
            index = lowercase_alphabet.index(letter)
            # Calculate the new index with the key
            new_index = (index + user_key) % 26
            # Append the corresponding letter from the alphabet to the coded message
            coded_message += lowercase_alphabet[new_index]
        else:
            # adds the white spaces to the encoded message
            coded_message += letter
    return coded_message



print(f"Encoded message: {encode(user_message_list, user_key)}")