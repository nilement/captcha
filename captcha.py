import pytesseract
import string
import requests
import pytesseract
import base64
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance, ImageFilter

siteUrl = 'http://challenge01.root-me.org/programmation/ch8/'
chars = string.digits + string.ascii_lowercase + string.ascii_uppercase

r = requests.get(siteUrl)
soup = BeautifulSoup(r.text, "html.parser").img['src'].split(',')[1]
imgdata = base64.b64decode(soup)
fileName = 'captcha.png'
with open(fileName, 'wb') as f:
    f.write(imgdata)

im = Image.open("captcha.png") 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp.png')
text = pytesseract.image_to_string(Image.open('temp.png'), config="-c tessedit_char_whitelist=" + chars +" -psm 6")
text = text.replace(" ", "")
print(text)