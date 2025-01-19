# Character Encoding
# https://ctflearn.com/challenge/115

# In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D

encodedValue = input("Please Enter: ")

listEncoded = encodedValue.split()
listDecoded = []
for i in listEncoded:
    listDecoded.append(chr(int(i,16))) #Converted the Hex Values to Integer Decimals and then converted the characters

print(''.join(listDecoded))