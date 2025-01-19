# Base 2 2 the 6
# https://ctflearn.com/challenge/192

# There are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9
# Reference: https://stackoverflow.com/questions/3470546/how-do-you-decode-base64-data-in-python

import base64

encodedString = input("Enter String: ")
print(base64.b64decode(encodedString))