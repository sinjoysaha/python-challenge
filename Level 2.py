import urllib.request

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
response = urllib.request.urlopen(url)
html = response.read()

print(response)

# print(html)

print("\nPrinting First few characters (from 500 to 2500):\n")
print(html[500:2500])

ss = str(html[500:])
# print(ss)

print("\nChecking character frequency:\n")
l = []
for i in range(256):
    l = l + [0]

for i in ss:
    ch = ord(i)
    l[ch] += 1

for i in range(256):
    if l[i] > 0:
        print(chr(i) + " : " + str(l[i]))


rl = "!#$%&()*+@[\]^_n{}"
new_ss = ""
for i in ss:
    if i not in rl:
        new_ss += i

print("\nAnswer:\n")
print(new_ss)
