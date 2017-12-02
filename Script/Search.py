import re
s = 'and'
words = re.findall(s, open('m2bahran.txt').read().lower())
#words = re.findall(s, 'You and me and her and him')
print(len(words))
