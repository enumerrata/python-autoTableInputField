# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from xpinyin import Pinyin
from fill_table import *

def is_title_td(td):
     if not td: return False
     for child in td.contents:
          if callable(child.split) and child != '\n':
               return True
     return False
