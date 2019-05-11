#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:26:40 2019

@author: ogulcan
"""
import re
import json
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist


def cleanAndTokenize(fil):
    # with open('..\media\\'+filename) as fil:
    data = json.load(fil)

    nltk.download('stopwords')
    nltk.download('punkt')

    '''
    data will come as json from FE with colnames(fileupload)
    
    -content
    -date
    -docid
    -source
    -title
    
    and create columns called tokens and tok 
    
    tokens in relative tokens tok is whole corpus
    
    tok column is deleted after operation
    
    and return frequency distiribution of tokens of whole corpus
    
    '''
    p = re.compile(r'nonascii|.com|^https?:\/\/.*[\r\n]*|<.*?>|[^a-zA-Z ]+')
    stop_words = stopwords.words("english")

    data["tokens"] = {}

    for docs in data["content"]:
        data["content"][docs] = str(data["content"][docs]).lower()
        data["content"][docs] = p.sub('', str(data["content"][docs]))
        data["content"][docs] = " ".join(data["content"][docs].split())
        data["tokens"][docs] = nltk.word_tokenize(str(data["content"][docs]))
        data["tokens"][docs] = [word.lower() for word in data["tokens"][docs] if word.isalpha() if
                                word not in stop_words]

    data["tok"] = nltk.word_tokenize(str(data["content"]))

    data["tok"] = [word.lower() for word in data["tok"] if word.isalpha() if word not in stop_words]
    dist = FreqDist(data["tok"])
    del data["tok"]
    js = dist.most_common(10)  # 10 is arbitrary I could send whole data and it can be deduced in FE
    # js =json.dumps(js)
    return js

# print(cleanAndTokenize("UK_afterJaccard.json"))

def cleanAndTokenizev2(filename):
    with open('..\media\\'+filename) as fil:
        data = json.load(fil)

    nltk.download('stopwords')
    nltk.download('punkt')

    '''
    data will come as json from FE with colnames(fileupload)

    -content
    -date
    -docid
    -source
    -title

    and create columns called tokens and tok 

    tokens in relative tokens tok is whole corpus

    tok column is deleted after operation

    and return frequency distiribution of tokens of whole corpus

    '''
    p = re.compile(r'nonascii|.com|^https?:\/\/.*[\r\n]*|<.*?>|[^a-zA-Z ]+')
    stop_words = stopwords.words("english")

    data["tokens"] = {}

    for docs in data["content"]:
        data["content"][docs] = str(data["content"][docs]).lower()
        data["content"][docs] = p.sub('', str(data["content"][docs]))
        data["content"][docs] = " ".join(data["content"][docs].split())
        data["tokens"][docs] = nltk.word_tokenize(str(data["content"][docs]))
        data["tokens"][docs] = [word.lower() for word in data["tokens"][docs] if word.isalpha() if
                                word not in stop_words]

    data["tok"] = nltk.word_tokenize(str(data["content"]))

    data["tok"] = [word.lower() for word in data["tok"] if word.isalpha() if word not in stop_words]
    dist = FreqDist(data["tok"])
    del data["tok"]
    js = dist.most_common(10)  # 10 is arbitrary I could send whole data and it can be deduced in FE
    # js =json.dumps(js)
    return js

print(cleanAndTokenizev2("UK_afterJaccard.json"))
