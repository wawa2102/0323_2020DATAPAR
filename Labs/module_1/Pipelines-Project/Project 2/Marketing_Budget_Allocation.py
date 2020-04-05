#STEP 0 : 
"""You are the CMO of a new startupo selling a new IOT than can protect surfers from all kind of shark attacks 
    when people are doing all kind of boarding sport. Here we will use a dataset to determine the top 10 countries you need to target for which board activity whith your FB ads.

For that we'll need those data :
    - Case Number
    - Country
    - Activity
    - Fatal (Y/N)
    - Species """

budget = int(input('As CMO of the startup how much you want to allocate in $ to promote your IOT for the 10 countries with the most attacks for all the borading sports by all kid of sharks ? => '))


#Import needed library
import pandas as pd
import numpy as np
import os


#STEP 1 : GET DATA function 
print(os.getcwd())

def acquisition ():
    df = pd.read_csv('data/GSAF5.csv', sep=',', encoding='ISO-8859-1')
    return df

df = acquisition()
print(df.head())

print(df.columns)

#STEP 2 : Clean function
#posts = posts.rename(columns={'Id':'postId','OwnerUserId':'userId'})

def clean_dataset(df):
        #First step we sect the columns we want to work with
        filtered_clean = df[['Case Number','Country', 'Activity', 'Fatal (Y/N)', 'Species ']]
       
        #We changed the name of columns with ' ' and so on 
        filtered_clean = filtered_clean.rename(columns={"Species ":"Species"})
        
        #We check the NaN values
        print(filtered_clean.isnull().sum())
        
        #We changed the NaN values to 'Null' to clean them 
        filtered_clean = filtered_clean[['Case Number', 'Country','Activity','Fatal (Y/N)','Species']] = filtered_clean[['Case Number', 'Country','Activity','Fatal (Y/N)','Species']].fillna('Null')
        print(filtered_clean.isnull().sum())
        
        #We clean Null values either by changing the value aither by dropping the rows
        
        #We can't replace the case number so we drop the row 
        print(filtered_clean[(filtered_clean['Case Number']=='Null')])
        filtered_clean.drop([1983], inplace=True)
        
        #We drop also Country
        filtered_clean = filtered_clean[filtered_clean['Country']!='Null']
        
        #We drop null values from Type attack
        filtered_clean = filtered_clean[filtered_clean['Fatal (Y/N)']!='Null']
        print(filtered_clean)
        
        #Now our data is ready for filtering
        return filtered_clean

filtered_clean = clean_dataset(df)

def wrangle(df):
        #We keep only activities link to a board like kite surfing, surfing ...
        wrangled_data = df[df['Activity'].str.contains('urfing', regex=False)]
        print(wrangled_data)
        
        #We keep accidents liked to sharks but all kind of sharks
        wrangled_data = wrangled_data[wrangled_data['Species'].str.contains('shark', regex=False)]
        return wrangled_data
    
wrangled_data = wrangle(filtered_clean)


def analyze(df):
    grouped = df.groupby(['Country','Activity'])['Case Number'].agg('count').reset_index()
    final = grouped.sort_values('Case Number',ascending=False).head(10)
    total_top_10 = final['Case Number'].sum()
    #mortality_top_10 = 
    global budget
    final['Budget of FB Ads ($)'] = (budget * final['Case Number'] / total_top_10).round(2)
    print(final)
    return final
    
analyzed_data = analyze(wrangled_data)
