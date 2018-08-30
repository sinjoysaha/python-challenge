import urllib.request, urllib, pickle

url = "http://www.pythonchallenge.com/pc/def/peak.html"
req = urllib.request.urlopen(url)
html = req.read()

print(html)

url = "http://www.pythonchallenge.com/pc/def/pickle.html"
req = urllib.request.urlopen(url)
html = req.read()

print(html)

url = "http://www.pythonchallenge.com/pc/def/banner.p"
req = urllib.request.urlopen(url)
html = req.read()

print(html)

data = pickle.loads(html)

for i in data:
    s = ""
    for j in i:
        s += j[0]*j[1]
    print(s)
