import sys

encoded_data = input()
result = ''

for place in encoded_data:
    if place.isupper():
        result += chr((ord(place)+13-65)%26+65)
    elif place.islower():
        result += chr((ord(place)+13-97)%26+97)
    else:
        result += place

print(result)