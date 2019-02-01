# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:12:38 2019

@author: HeavyD
"""

from textblob import TextBlob
import random
import re
with open('ww2.txt','r') as article:
    art=article.read()
art.replace('\n','')
artb=TextBlob(art)
sent={}
for sentence in artb.sentences:
    parts={}
    sent[sentence.string]=parts;
    for t in sentence.tags:
        tag=t[1]
        if tag not in parts:
            parts[tag]=[]
        parts[tag].append(t[0]) 
    sent[sentence.string]=parts;    
def putspace(word,sentence):
    reword=re.compile(word)
    return reword.sub("______",sentence)
def remove(sentence,parts):
    partsofspeech=None
    if "NNP" in parts:
        partsofspeech=parts['NNP']
    elif "NN" in parts:
        partsofspeech=parts['NN']
    else:
        print("nouns and proper nouns not found")
    if len(partsofspeech)>0:
        word=random.choice(partsofspeech)
        newsent=putspace(word,sentence)
        return (word,sentence,sent)
    else:
        print("words are empty")
for sentence in sent.keys():
    partsos = sent[sentence]
    (word, oldsentence, newsent) = remove(sentence, partsos)
    if newsent is None:
        print ("Founded none for ")
        print(sentence)
    else:
        print(newsent)
        print ("\n===============")
        print(word)
        print ("===============")
        print("\n")
    
        

        
            
    
   