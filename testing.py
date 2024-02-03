import random

# Define character sets
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
symbols = "~ #^*_/<>|`"

# Stats
roll = 1
intelligence = 2
dexterity = 2

# Set the BASE number of characters and symbols
base_num_characters = 1
base_num_symbols = 7

# calculate number of characters based off of intelligence attribute
num_characters = (roll - intelligence) * base_num_characters + 4

# calculate number of symbols based off of dexterity attribute
if dexterity < 0: 
    num_symbols = (roll * abs(dexterity)) + 4
else: 
    num_symbols = (roll - abs(dexterity)*2) + 4

# Generate encrypted message
encrypted_message = ''.join(random.choice(chars) for _ in range(num_characters))
encrypted_message += ''.join(random.choice(symbols) for _ in range(num_symbols))

# Shuffle the encrypted message
encrypted_message_list = list(encrypted_message)
random.shuffle(encrypted_message_list)
encrypted_message = ''.join(encrypted_message_list)

# Decrypt message by removing symbols
decrypted_message = encrypted_message.translate(str.maketrans("", "", symbols))

# Display results
print(f"+{'=' * 30}+")
print(f"Chars: {num_characters}|Symbols: {num_symbols}")
print("Encrypted Message:", encrypted_message)
print(f"+{'=' * 30}+")

inp = input("Decode the message: ")
if inp == decrypted_message:
    print("YOU WIN")
else:
    print("YOU LOSE")
