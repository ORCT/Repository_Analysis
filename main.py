from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('\nhttps://github.com/ORCT/Capstone')#add \n first
bs = BeautifulSoup(html, 'html.parser')

f = open('url_html.txt', 'w', encoding = 'utf-8')
f.write(str(bs))
f.close()