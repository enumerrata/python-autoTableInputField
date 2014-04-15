# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('2_strip.htm',encoding='utf-8'),from_encoding='utf-8')
print("fuck")
for p in soup.find(id='_content').p:
     print(p)
#print(soup.prettify())
##f = open('prase1-lite.htm','w',encoding='utf-8')
##f.write(str(soup))
##f.close()
