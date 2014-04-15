# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from xpinyin import Pinyin


soup = BeautifulSoup(open('prase1.htm',encoding='utf-8'),from_encoding='utf-8')
print("fuck2")
i = 1
mulu = open('mulu.txt',encoding='utf-8')
for line in soup.find_all('p'):
     for s in line.stripped_strings:
          if ((s.find('检表') == 0) or (s.find('统计表') == 0)):
               if (s.find('检表') == 0):
                    table_type = '检表'
                    num = str(i-7)
               else:
                    table_type = '统计表'
                    num = str(i)
               new_tag = soup.new_tag('table')
               new_tag['class'] = 'titleTb'
               new_tag_tr = soup.new_tag('tr')
               new_tag_tr['class'] = 'norTR'
               new_tag_td1 = soup.new_tag('td', style='width: 1mm;')
               new_tag_td1_label = soup.new_tag('label', id='_tbName')
               new_tag_td1_label.append(table_type+num)
               new_tag_td1.append(new_tag_td1_label)
               new_tag_tr.append(new_tag_td1)
               new_tag_td2 = soup.new_tag('td', style='width: 100mm;')
               new_tag_td2_label = soup.new_tag('label', id='_tbTitle')
               new_tag_td2_label.append(mulu.readline())
               new_tag_td2.append(new_tag_td2_label)
               new_tag_tr.append(new_tag_td2)
               new_tag.append(new_tag_tr)
               line.replace_with(new_tag)
               i += 1
               break
print(i)
for line in soup.find_all(class_='MsoNormalTable'):
     #print(line.next_sibling.next_sibling)
     p = line.next_sibling.next_sibling
     new_tag_tr = soup.new_tag('tr')
     new_tag_tr['class'] = 'norTr'
     new_tag = soup.new_tag('table')
     new_tag['class'] = 'footTb'
     new_tag.append(new_tag_tr)
     for sub in p.stripped_strings:
          for s in sub.splitlines():
               if len(s.strip()) > 1:
                    #print(s+'#')
                    new_tag_td = soup.new_tag('td', style="width:1cm;")
                    if len(s.strip(':')) > 2:
                         new_tag_td['style'] = "width:15mm;"
                    new_tag_td_ip = soup.new_tag('td', style=new_tag_td['style'])
                    pinyin = Pinyin()
                    s = s.strip(':').strip('：').strip()
                    pys = pinyin.get_init(s) 
                    new_tag_ip = soup.new_tag('input', id= 'ft_'+pys)
                    new_tag_td_ip.append(new_tag_ip)
                    new_tag_td.append(soup.new_string(s+':'))
                    new_tag_tr.append(new_tag_td)
                    new_tag_tr.append(new_tag_td_ip)
     p.replace_with(new_tag)
for line in soup.find_all('p'):
     line.unwrap()
print(soup.prettify())
f = open('prase2.htm','w',encoding='utf-8')
f.write(soup.prettify())
