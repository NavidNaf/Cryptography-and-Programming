# Hextroadinary
# https://ctflearn.com/challenge/158

# Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? Your answer should start with 0x. 0xc4115 0x4cf8

binVal1 = bin(int(input(),16)) # Converting the Hex Input to Binary
binVal2 = bin(int(input(),16))
print(hex((int(binVal1, 2) ^ int(binVal2, 2)))) # Perfroming XOR (^ operator) and then Converting back to hex