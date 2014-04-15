# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('origin.htm',encoding='utf-8'),from_encoding='utf-8')
print("fuck")
#soup.style.decompose()
for line in soup.find_all(['span','font','div','br']):
     line.unwrap()
for line in soup.find_all('tr', height='0'):
     line.decompose()
for line in soup.find_all('td', width='0'):
     line.decompose()
for line in soup.find_all(['td', 'tr']):
     del line['style']
     del line['valign']
     del line['height']
     del line['width']
for line in soup.find_all('tbody'):
     line.unwrap()
print(soup.prettify())
f = open('prase1.htm','w',encoding='utf-8')
f.write(soup.prettify())
