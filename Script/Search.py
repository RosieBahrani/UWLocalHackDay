import re
s = 'and'
words = re.findall(s, open('r35yan.txt').read().lower())
#words = re.findall(s, 'You and me and her and him')
print(len(words))
