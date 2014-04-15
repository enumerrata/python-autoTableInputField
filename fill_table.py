# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from xpinyin import Pinyin

def get_tr_width(tr):
     result = 0
     for td in tr.find_all('td'):
          if td.get('colspan'):
               colspan = int(td.get('colspan'))
          else:
               colspan = 1
          result += colspan
     return result
     
def get_title_pinyin_td(td):
     py = Pinyin()
     result = get_title_td(td)
     result = py.get_init(result)
     return result

def is_title_td(td):
     if not td: return False
     for child in td.contents:
          if callable(child.find) and child != '\n' and child.find('签名') == -1:
               return True
     return False

def get_title_td(td):
     for child in td.contents:
          if callable(child.split) and child != '\n':
               result = ''.join(child.replace('\n','').split('(')[0].split('（')[0].split())               #print(''.join(child.replace('\n','').split('(')[0].split()))
               return result

def is_title_tr(tr):
     num_title = 0
     num_td = len(list(tr.find_all('td')))
     for td in tr.find_all('td'):
          if is_title_td(td):
               num_title += 1
     if num_title == num_td > 1:
          return True
     return False

def is_cupple_row_tr(tr):
     num_title = 0
     num_td = len(list(tr.find_all('td')))
     flag = 1
     for td in tr.find_all('td'):
          if is_title_td(td):
               if flag >1:
                    return True
               flag = 1
          if not is_title_td(td):
               flag += 1

     return False

def is_unfill_row_tr(tr, tlist):
     flag = 1
     if get_tr_width(tr) != tlist['width']:
          return False
     for td in tr.find_all('td'):
          if is_title_td(td):
               flag = 1
          else:
               flag += 1
          if flag > 2:
               return True
     return False

def get_title(tr):
#tr is the first tr
     t = {'height':0,'list':[],'width':0}
     for td in tr.find_all('td'):
          if td.get('colspan'):
               colspan = int(td.get('colspan'))
          else:
               colspan = 1
          if td.get('rowspan'):
               rowspan = int(td.get('rowspan'))
          else:
               rowspan = 1
          t['width'] += colspan
          if (t['height'] < rowspan):
               t['height'] = rowspan
          for i in range(colspan):
                    t['list'].append({'title':get_title_pinyin_td(td),'idle': t['height']-rowspan})
     for i in range(t['height']-1):
          tr = tr.next_sibling.next_sibling
          if is_title_tr(tr):
               for td in tr.find_all('td'):
                    for item in t['list']:
                         if item['idle'] >= t['height']-1-i:
                              index = t['list'].index(item)
                              break
                    if td.get('colspan'):
                         colspan = int(td.get('colspan'))
                    else:
                         colspan = 1
                    if td.get('rowspan'):
                         rowspan = int(td.get('rowspan'))
                    else:
                         rowspan = 1
                    for j in range(colspan):
                         t['list'][j+index]['title'] += '_'+get_title_pinyin_td(td)
                         t['list'][j+index]['idle'] -=rowspan

          #print(t)
     return t
          
def fill_tr(tr, title, i):
     width = 0
     n = 0
     for td in tr.find_all('td'):
          if td.get('colspan'):
               colspan = int(td.get('colspan'))
          else:
               colspan = 1
          if not is_title_td(td):
               if n ==0:
                    try:
                         if title['list'][width]['title'] == title['list'][width+colspan]['title']:
                              n += 1
                         else:
                              n = 0
                    except:
                         pass
               else:
                    tp = td.find_previous_sibling('td')
                    if tp.get('colspan'):
                         pcolspan = int(tp.get('colspan'))
                    else:
                         pcolspan = 1
                    if title['list'][width]['title'] == title['list'][width-pcolspan]['title']:
                         n += 1
                    else:
                         n = 0
               tag_id = title['list'][width]['title']
               if tag_id[-1].isdigit():
                    tag_id += '_'
               tag_id += str(i)
               new_tag = BeautifulSoup().new_tag('input',id=tag_id)
               if n > 0:
                    new_tag['id'] += '_'+str(n)
               new_tag['value'] = new_tag['id']
               if td.input:
                    td.input.replace_with(new_tag)
               else:
                    td.append(new_tag)
          width += colspan

def fill_cupple_tr(tr):
     for td in tr.find_all('td'):
          if is_title_td(td):
               k = td.next_sibling.next_sibling
               if k and (not is_title_td(k)):
                    if get_title_td(td).find('意见') != -1:
                         new_tag = BeautifulSoup().new_tag('textarea',id=get_title_pinyin_td(td))
                         new_tag['rows'] = 20
                         new_tag.clear()
                    else:
                         new_tag = BeautifulSoup().new_tag('input',id=get_title_pinyin_td(td))
                         new_tag['value'] = new_tag['id']
                    if k.input:
                         k.input.replace_with(new_tag)  
                    else:
                         k.append(new_tag)

def fill_table(tb):
     have_title = False
     for tr in tb.find_all('tr'):
          if is_title_tr(tr) and len(list(tr.find_all('td'))) > 2:
               title = get_title(tr)
               have_title = True
               break
     i = 1
     for tr in tb.find_all('tr'):
          if have_title and is_unfill_row_tr(tr,title):
               fill_tr(tr, title, i)
               i += 1
          elif not (is_title_tr(tr)):
               fill_cupple_tr(tr)
     return have_title

def fill_file(filename,input_dir='input',output_dir='output'):
     soup = BeautifulSoup(open(input_dir+'/'+filename,encoding='utf-8'),from_encoding='utf-8')
     #print(soup)
     result =  True
     for bodytb in soup.find_all(class_='bodyTb'):
          try:
               result = fill_table(bodytb)
               #print(filename,"\tOK")
          except (UnboundLocalError,AttributeError):
               result =  False
          break
     out = open(output_dir+'/'+filename,'w',encoding='utf-8')
     out.write(soup.prettify())
     out.close()
     return result
