import urllib.request, re

url = "http://www.pythonchallenge.com/pc/def/equality.html"

response = urllib.request.urlopen(url)
html = response.read()

#print(html)
ss = str(html)

print(ss[:2000])

f = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',ss)
print(f)

new_ss = ""
for i in f:
    new_ss += i[4]

print(new_ss)
