import re
import pprint
import collections

data = open("News.txt", "r")
s = data.read()
data.close()

c = collections.Counter(s)

pprint.pprint(c)
