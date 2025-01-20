import cv2
import pytesseract
from PIL import Image
import sys

# Set the path for tesseract (adjust based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract" 

# Load the image using OpenCV
image = cv2.imread(sys.argv[1])

# Preprocess the image (convert to grayscale and apply thresholding)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)

noiseless_image = cv2.medianBlur(thresh_image, 5)

text = pytesseract.image_to_string(noiseless_image)

# Filter out non-numeric characters
numbers = text.split()

# assuming that the format is like PICOCTF{}. cleaning the number
numbers.pop(0)
numbers.pop(0)
numbers.pop(1)
numbers.pop(3)
numbers.pop(3)

numb = ''.join(numbers)
print(numb)

#### logics can't separate this, but loved the OCR part so keeping that. 

## Actual solution

ciphertext = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'

cipherList = ciphertext.split()
print(cipherList)

decrypt = ""
for char in cipherList:
    if char.isdigit():
        decrypt += chr(int(char) + 64)
    else:
        decrypt += char

print(decrypt)