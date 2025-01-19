# Convert hex to base64
# https://cryptopals.com/sets/1/challenges/1

from base64 import b64encode, b64decode

hex_code = input()

b64 = b64encode(bytes.fromhex(hex_code)).decode()
print(b64)