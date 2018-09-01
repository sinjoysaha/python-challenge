# Solution 1

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
ss = ""
for i in s:
    ch = ord(i)
    if ch < 97 or ch > 122:
        ss = ss + i
    else:
        ss = ss + chr((((ch + 2) - 96) % 26) + 96)

print("For Solution 1:")
print(ss)

# Solution 2

a = "abcdefghijklmnopqrstuvwxyz"
b = "cdefghijklmnopqrstuvwxyzab"
tr = str.maketrans(a, b)
print("\nFor Solution 2:")
print(s.translate(tr))

url = "http://www.pythonchallenge.com/pc/def/map.html"
url2 = "map"
print(url.translate(tr))
print(url2.translate(tr))
