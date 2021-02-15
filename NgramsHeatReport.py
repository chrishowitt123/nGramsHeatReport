# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 23:41:23 2021

@author: chris
"""

import docx2txt
from termcolor import colored
import tkinter
from tkinter import filedialog
from nltk.util import everygrams
import pprint
import pandas as pd

pp = pprint.PrettyPrinter(indent=4)

# root = tkinter.Tk()
# root.wm_withdraw() # this completely hides the root window
# file = filedialog.askopenfilename()

file = r"C:\Users\chris\Desktop\RepStrindsGroups\Dossier_Emitentes_V2.docx"

text = docx2txt.process(file)
# print(text)

paras = text.split('\n')

paras = [x for x in paras if x]


allNgrams = []

for p in paras:
    p_split = p.split()
    allNgrams.append(list(everygrams(p_split)))
    
    
# for grams in allNgrams:
#     print(grams) 
#     print('\n')
#     print('\n')

allNgramsList = []

for phrase in allNgrams:
    for gram in phrase:
        allNgramsList.append(list(gram))
        

allNgramsStrings = ([' '.join(e).lower() for e in allNgramsList])


gramsDict = {}
for gram in allNgramsStrings:
    count = allNgramsStrings.count(gram)
    gramsDict[gram] = count

df = pd.DataFrame(list(gramsDict.items()),columns = ['Grams','Count'])
df['String_Lengths'] = len(df['Grams'])
df.sort_values((['String_Lengths']),ascending=False )
print(df)
df.to_excel('nGrams.xlsx')