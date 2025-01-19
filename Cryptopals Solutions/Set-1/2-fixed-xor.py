binVal1 = bin(int(input(),16)) # Converting the Hex Input to Binary
binVal2 = bin(int(input(),16))
print(hex((int(binVal1, 2) ^ int(binVal2, 2)))[2:]) # Perfroming XOR (^ operator) and then Converting back to hex