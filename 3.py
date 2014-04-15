# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from xpinyin import Pinyin


soup = BeautifulSoup(open('prase2.htm',encoding='utf-8'),from_encoding='utf-8')
print("fuck3")
for line in soup.find_all(class_='MsoNormalTable'):
     del line['style']
     del line['border']
     del line['cellpadding']
     del line['cellspacing']
     line['class'] = 'bodyTb'
     line['style'] = 'border-width: 0 0 0 1px;'
     for tr in line.find_all('tr'):
          tr['class'] = 'norTr'

print(soup.prettify())
f = open('prase3.htm','w',encoding='utf-8')
head = '''<!--__js_start__-->
<script type="text/javascript" src="../orgTable.js"></script>
<!--__js_end__-->
<!--__css_start__-->
<link rel="stylesheet" type="text/css" href="../orgTable.css"/>
<style type="text/css">
</style>
<!--__css_end__-->
'''
f.write(head)
f.write(soup.prettify())
