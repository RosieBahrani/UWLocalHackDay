import urllib
from bs4 import BeautifulSoup as BS

html =urllib.urlopen('url').read()

soup = BS(html)


print (soup.find('div',{'class':'drkgry'})[1].get_text())
