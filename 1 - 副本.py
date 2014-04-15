# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('2.htm',encoding='utf-8'),from_encoding='utf-8')
print("fuck")
for line in soup.find_all('table'):
     del line['border']
     if line.get('style'):
          index = line['style'].find('border:')
          line['style'] = line['style'][:index]
for line in soup.find_all(['br','font','div']):
     line.unwrap()
#for line in soup.find_all('tr', height='0'):
     #line.decompose()
#for line in soup.find_all('td', width='0'):
#     line.decompose()
for line in soup.find_all('p'):
     del line['align']
for line in soup.find_all('td'):
     del line['valign']
     if line.get('style'):
          index = line['style'].find('width:')
     if index != -1:
          line['style'] = line['style'][index:].split(';')[0]+';'
     else:
          del line['style']
for line in soup.find_all('span'):
     del line['lang']
     if line.get('style'):
          index = line['style'].find('font-size:')
          if index != -1:
               line['style'] = line['style'][index:].split(';')[0]+';'
          else:
               del line['style']
for line in soup.find_all('tr', height='0'):
          line['class'] = 'tbFix'
print(soup.prettify())
f = open('2-strip.htm','w',encoding='utf-8')
f.write(str(soup))
f.close()
