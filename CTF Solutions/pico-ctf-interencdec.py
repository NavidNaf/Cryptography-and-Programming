import sys
import base64
import re

# Open the file and read the file
with open(sys.argv[1], 'r') as file:
    enc_text=file.read()

# decode the base64
level_one_b = base64.b64decode(enc_text)
level_one = level_one_b.decode('ascii')

match = re.search(r"b['\"]([^'\"]+)",level_one)

if match:
    new_enc_text = match.group(1)

# decode the newly found base64
level_two_b = base64.b64decode(new_enc_text)
level_two = level_two_b.decode('ascii')

# bruteforce caesar
for shift in range(1,26):
    result = ''
    for placeholder in level_two:
        if placeholder.isupper():
            result += chr((ord(placeholder)+ shift - 65)%26+65)
        elif placeholder.islower():
            result += chr((ord(placeholder)+ shift - 97)%26+97)
        else:
            result += placeholder
    match_two = re.search(r"^pico", result)
    if match_two:
        decrypted = match_two.group(0)
        print(result)