import re
s = 'and'
words = re.findall(s, open('/Users/mahshidbahrani/Downloads/Unknown-15').read().lower())
#words = re.findall(s, 'You and me and her and him')
print(len(words))
