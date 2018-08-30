import urllib.request, re

req = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php")
html = req.read()

ss = str(html)
print(ss)

prev = "8022" #Replace when divide by two appears :D

for i in range(400):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+prev
    req = urllib.request.urlopen(url)
    html = req.read()
    
    ss = str(html)
    print(ss)
    m = re.findall(r'next nothing is [0-9]{1,}',ss)[0]
    prev = re.findall(r'[0-9]{1,}',m)[0]
    print(prev)
    
