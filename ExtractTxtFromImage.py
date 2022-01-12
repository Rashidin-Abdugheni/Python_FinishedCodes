from PIL import Image
import PIL.Image  # pip install Pillow

from pytesseract import image_to_string
# Import modules
from PIL import Image
import pytesseract

# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Create an image object of PIL library
image = Image.open('C:\\Users\\Administrator\\Desktop\\1.PNG')

# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')

# Print the text
print(image_to_text)

# write the result in to a txt file
f = open (r'C:\\Users\\Administrator\\Desktop\\all.txt','w')

print (image_to_text,file = f)

f.close()