from urllib.request import urlopen
import bz2

html = urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").read()

ss = str(html)

print(ss)

un = ss.split("nun: \\'")[1]
pw = un.split("npw: \\'")[1]
un = un.split("npw: \\'")[0]

print(un)
print(pw)

un = un.split("\\")[0:-2:2]
pw = pw.split("\\")[0:-2:2]

un = "\\".join(un)
pw = "\\".join(pw)
print(un)
print(pw)

# Initial BZh91AY&SYA refers to bz compression

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un))
print(bz2.decompress(pw))
