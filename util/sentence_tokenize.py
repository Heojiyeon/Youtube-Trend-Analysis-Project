from PyKomoran import *
import pandas as pd
komoran=Komoran(DEFAULT_MODEL['FULL'])
data=pd.read_csv('dataset/KRvideos.csv', engine='python')
df=data[:]
yt_description=df['description']
yt_tags=df['tags']
yt_title=df['title']


def data_tokenize(df):
    temp=[]
    for i in range(len(df)):
        sentence=df[i]
        sentence_nouns=komoran.get_morphes_by_tags(sentence, tag_list=['NNG','NNP','NNB','NP','NR','VV','VA','VC','MM','MA'])
        temp.append(sentence_nouns)
    return temp
def sentence_tokenize(sentence):
    sentence_nouns=komoran.get_morphes_by_tags(sentence, tag_list=['NNG','NNP','NNB','NP','NR','VV','VA','VC','MM','MA'])
    return sentence_nouns

