import os
from config import Config as c
myemail = c.myemail

import json
import requests




# convert word_data to a stripped and stemmed form
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
# stemming
stemmer = SnowballStemmer("english")
tokenizer = RegexpTokenizer(r'\w+')

def strip_stem(s): # removes punctuation and stems words
    s = ''.join([i for i in s if not i.isdigit()]) # remove numbers
    s = s.encode("ascii", errors="ignore").decode() # remove non ascii chars
    s = tokenizer.tokenize(s) #tokenize according to the above stemmer/tokenizer
    return ' '.join([stemmer.stem(word.lower()) for word in s if len(word)>=3]) # stem and omit short words 



def get_dimensions(doi, dim_data):
    try:
        out = dim_data[doi]
    except:
        base= 'http://metrics-api.dimensions.ai/doi/'
        r = requests.get(base+doi)
        out = r.json()
        dim_data[doi] = out
    return out, dim_data

def build_dim_data(dois,dim_data_p, dim_failures_p):
    try:
        with open(dim_data_p,'rb') as f:
            dim_data = json.loads(f.read())
        successes = list(dim_data.keys())
        print('Reading cached data for {} articles'.format(len(successes)))

    except:
        print('Cache not found.')
        print('Creating new cache.')
        dim_data = {}
        with open(dim_data_p,'wb') as f:
            f.write(b'{}') 
        successes=[]

    try:
        with open(dim_failures_p,'rb') as f:
            failures = json.loads(f.read())

    except:
        failures = []
        with open(dim_failures_p,'wb') as f:
            f.write(b'[]') 
    i=0
    for doi in dois:
        if doi in successes:
            i+=1
            continue
        if i%1000==0:
            print('Dimensions data retrieved for: ',i,'/',len(dois),' articles')
        try:
            doi_dim_data, dim_data = get_dimensions(doi, dim_data)
        except:
            if doi not in failures:
                failures.append(doi)
        else:
            pass
        i+=1
    # write data to files
    print('Writing Dimensions data to file.')
    with open(dim_data_p,'w+') as f:
        f.write(json.dumps(dim_data))
    with open(dim_failures_p,'w+') as f:
        f.write(json.dumps(failures))        
            
    print('Dimensions data written to file')

###############################################################
##  CrossRef
###############################################################
    
def get_cr_data(doi, cr_data, myemail):
    try:
        out = cr_data[doi]
    except:
        print('Data for ',doi,' not available in cache.  Querying CrossRef API')
        url = 'http://api.crossref.org/works/'
        mailto = '?mailto={}'.format(myemail) # myemail variable is imported at the top
        q = url+doi+mailto
        req = requests.get(q)
        out = req.json()
        cr_data[doi] = out
    return out, cr_data

def build_cr_data(dois, cr_data_p):
    
    # initialise
    print('Reading CrossRef data from cache')
    try:
        with open(cr_data_p,'rb') as f:
            cr_data = json.loads(f.read())
        successes = list(cr_data.keys())
        print('Reading cached data for {} articles'.format(len(successes)))

    except:
        print('Cache not found!')
        print('Creating new cache.')
        cr_data = {}
        with open(cr_data_p,'wb') as f:
            f.write(b'{}') 

    # acquire
    
    i=0
    for doi in dois:
        if doi in successes:
            i+=1
            continue
        if i%1000==0:
            print('CrossRef data retrieved for: ',i,'/',len(dois),' articles')
        try:
            doi_cr_data, cr_data = get_cr_data(doi, cr_data, myemail)
        except:
            pass
        i+=1
    print('Writing CrossRef data to file.')
    with open(cr_data_p,'w+') as f:
        f.write(json.dumps(cr_data))
    print('CrossRef data written to file.')