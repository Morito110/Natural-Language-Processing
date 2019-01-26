import re
import pprint
import collections

data = open("News.txt", "r")
s = data.read()
data.close()

c = re.sub(r'[^a-zA-Z\n]', ' ', s)
#c = re.sub(r'[0-9]', ' ', s)
#c = collections.Counter(s)

print(c)
#pprint.pprint(c)
