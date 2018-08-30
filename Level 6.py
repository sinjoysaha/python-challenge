from urllib.request import urlopen
import re, zipfile

html = urlopen("http://www.pythonchallenge.com/pc/def/channel.html").read()
print(html)

#Replace with zip
#Replace html with zip

'''
prev = "90052"

for i in range(911):
    filename = "channel/"+prev+".txt"
    file = open(filename,'r')
    ss = file.read()
    print(ss)
    prev = re.findall(r'[0-9]{1,}',ss)[0]
    print(prev)
'''

#Getting both the numbers and comments

f = zipfile.ZipFile("channel.zip")

prev = "90052"
comments = []
for i in range(908):
    ss = f.read(prev+".txt").decode("utf-8")
    comments += [f.getinfo(prev+".txt").comment.decode("utf-8")]
    print(ss)
    prev = re.findall(r'[0-9]{1,}',ss)[0]
    print(prev)

print("".join(comments))
