# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:59:48 2021

@author: chris
"""

from itertools import tee, islice
import docx2txt
from collections import Counter
import re
from termcolor import colored
from functools import reduce
import pprint
pp = pprint.PrettyPrinter(indent=4)
import nltk
nltk.download('punkt')

file = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\384180221_TM_JTI\Translation\MY COPY_binder EN.docx"

text = docx2txt.process(file)
words = nltk.word_tokenize(text)




def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break    
  


n = 5


gramsDall= []


    

gramsD = dict(Counter(ngrams(words, n)))
gramsD

for key, value in gramsD.items():
    if value > 3:
        print(key, value)
        
c = Counter(gramsD)
pp.pprint(c.most_common())
