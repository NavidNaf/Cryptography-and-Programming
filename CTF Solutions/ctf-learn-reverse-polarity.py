# Reverse Polarity
# https://ctflearn.com/challenge/230

# I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101


# You can take each block of eight characters (a byte), convert that to an integer, and then convert that to a character with chr()
from textwrap import wrap
reverseVal = input("Enter Value: ")
listofeight=wrap(reverseVal, 8)

message=''
for i in listofeight:
    val=chr(int(i,2))
    message += val

print(message)