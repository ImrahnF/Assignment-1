import random

# generate message
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
symbols = "~!@#$%^&*()_+-=/.,<>?;:[]|`"

num_characters = 10
num_symbols = 5

decypted_message = ""
encrypted_message = ""

# add characters to the message
for i in range(num_characters):
    encrypted_message += random.choice(chars)

# add symbols
for i in range(num_symbols):
    encrypted_message += random.choice(symbols)

# shuffle the message and turn it back in to a string
encrypted_message = list(encrypted_message)
random.shuffle(encrypted_message)
encrypted_message = ''.join(encrypted_message)

# Create a translation table to show decrypted message
translation_table = str.maketrans("", "", symbols)
decypted_message = encrypted_message.translate(translation_table)

# finish
print(encrypted_message)
print(decypted_message)
