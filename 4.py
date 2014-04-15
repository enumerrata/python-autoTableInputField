# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from xpinyin import Pinyin
import shutil
import os

soup = BeautifulSoup(open('2-strip.htm',encoding='utf-8'),from_encoding='utf-8')
print("fuck4")
i = 1
print("手动添加_content")
try:
     shutil.rmtree('part')
except:
     pass
os.mkdir('part')
for part in soup.find_all(id='_content'):
     
     head =  BeautifulSoup('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=uft-8" />
<title>zpb1</title>
<!--__js_start__-->
<script type="text/javascript" src="../orgTable.js"></script>
<!--__js_end__-->
<!--__css_start__-->
<link rel="stylesheet" type="text/css" href="../orgTable.css"/>
<style type="text/css">
</style>
<!--__css_end__-->
</head>
<body></body></html>''')
     head.body.append(part)
     if i < 8:
          fname = 'tjb' + str(i)
     else:
          fname = 'jb'+str(i-7)
     head.title.string = fname
     #print(head.title)
     f = open('part/'+fname +'.html','w',encoding='utf-8')
     f.write(str(head))
     f.close()
     print(i)
     i += 1
f = open('prase4.htm','w',encoding='utf-8')
f.write(BeautifulSoup(open('prase3.htm',encoding='utf-8'),from_encoding='utf-8').prettify())
