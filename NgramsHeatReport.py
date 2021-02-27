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
import nltk
nltk.download('punkt')

file = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\385240221_TM_HS\Orignals\COPY_Caracterização da vegetação ao longo das futuras linhas de transmissão de energia Lubango.docx"

text = docx2txt.process(file)
words = nltk.word_tokenize(text)

paras = text.split('\n')
paras = [x for x in paras if x]
paras = [p.replace('\t', '') for p in paras]
parasSplit = [p.split(' ') for p in paras]


pLengths = []
for p in paras:
    pLengths.append(len(p))
    
pLengths.sort(reverse = True)


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
  


n = 3


gramsDall= []


    
for p in parasSplit: 
    gramsD = dict(Counter(ngrams(p, n)))
#         gramsD = {k:v for (k,v) in gramsD.items() if v > 1} 
#     print(gramsD)
#     print(p)
    gramsDall.append(gramsD)
    if n <= pLengths[0]:
        n+=1
    else:
        break
        

gramsDall = list(filter(None, gramsDall))
gramsDall

for d in gramsDall:
    for k, v in d.items():
        ''.join(k)


gramsSwap = reduce(lambda a, b: {**a, **b}, gramsDall)
# gramsSwap

# res = dict((v,k) for k,v in gramsSwap.items())


#res

stringList = list(gramsSwap.keys())
stringList

stringList = [list(elem) for elem in stringList]


stringList

    
stringList = [' '.join(x) for x in stringList]


for index, item in enumerate(stringList):
    print(index, len(item.split(' ')), item)
    
Counter(stringList)
