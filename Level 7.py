from urllib.request import urlopen
from PIL import Image
from io import BytesIO
import requests

html = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.html").read()

ss = str(html)
print(ss)

img = Image.open(BytesIO(requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content))

w = img.width
h = img.height
row = []
for i in range(w):
    row += [img.getpixel((i, h/2))]

print(row)
#Discarding duplicates
print()
row = row[::7]
print(row)

new_ss = ""
for i in row:
    new_ss += chr(i[0])
print(new_ss)

next_ss = new_ss[43:-4].split(", ")
print(next_ss)

next_level = ""
for i in next_ss:
    next_level += chr(int(i))

print(next_level)
