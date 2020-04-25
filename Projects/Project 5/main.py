print('BIENVENUE')

import pandas as pd
import requests as r
import json
import time
import matplotlib.pyplot as plt
import re

data_w = pd.read_csv("2120116_V2.csv", sep=";")
data_v = pd.read_csv("vivino.csv", sep=",")

#check
#print(data_w.head())
#print(data.columns)
#print(data.shape)
#print(data.describe())
#print(data['NAME'].value_counts())

#print(data[data['NAME']=='REIMS PRUNAY, FR'].groupby('DATE').count())
#print(data.NAME.value_counts())

#df.DATE[(df.NAME=='REIMS PRUNAY, FR')]

dct_stations = {'bordeaux': 'BORDEAUX MERIGNAC, FR',
       'languedoc-roussillon':  'MONTPELLIER AEROPORT, FR',
       'cote-de-beaune': 'DIJON LONGVIC, FR',
       'cote-de-nuits': 'DIJON LONGVIC, FR' ,
       'rhone': 'LYON ST EXUPERY, FR',
       'loire-valley': 'NANTES BOUGUENAIS, FR' 'CLERMONT FERRAND, FR',
       'bourgogne': 'DIJON LONGVIC, FR',
       'champagne': 'REIMS PRUNAY, FR',
       'alsace': 'STRASBOURG ENTZHEIM, FR',
       'chateauneuf-du-pape': 'MONTELIMAR, FR'}

### READ DF VIVINO

data_v['station']=data_v["vintage.wine.style.region.seo_name"].map(dct_stations)

#print(data_v.head())

#print(data_v.groupby('station').count())

def liste(c):
    N=[]
    for i in range(1,13):
        if i<10 :
            N.append(str(c)+str('-')+str(0)+str(i))
        else : 
            N.append(str(c)+str('-')+str(i))
    return N

def splitDataFrameList(df,target_column,separator):
    ''' df = dataframe to split,
    target_column = the column containing the values to split
    separator = the symbol used to perform the split
    returns: a dataframe with each entry for the target column separated, with each element moved into a new row. 
    The values in the other columns are duplicated across the newly divided rows.
    '''
    def splitListToRows(row,row_accumulator,target_column,separator):
        split_row = row[target_column]
        for s in split_row:
            new_row = row.to_dict()
            new_row[target_column] = s
            row_accumulator.append(new_row)
    new_rows = []
    df.apply(splitListToRows,axis=1,args = (new_rows,target_column,separator))
    new_df = pd.DataFrame(new_rows)
    return new_df

data_v['Year'] = data_v.apply(lambda row:(liste(row['vintage.year'])),axis=1)

data_v=splitDataFrameList(df=data_v, target_column="Year",separator=",")

#print(data_v.info())

data_v['join']=data_v.apply(lambda row:(str(row['station'])) +((str(row['Year']))),axis=1)
data_w['join']=data_w.apply(lambda row:(row['NAME'])+(row['DATE']),axis=1)
####### JOIN

#print(data_v['join'][0])
#print(data_w['join'][0])

#data_full = data_v.join(data_w, lsuffix='_caller', rsuffix='_other')

#data_full.to_csv("data_full_V1.csv", index = False)

data=data_v.merge(data_w,on='join')

print(data.info())

#result = pd.merge(data_v,  data_w,  on ='join_caller',  how ='inner') 

print(data.head(1))