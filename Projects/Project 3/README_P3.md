# Iron Hack - Project 3 - Web Scrapping

Context : As a data analyst you will build a scrapping tool to help authors to write the good stories and marketing officer to push those stories to the right persons. 

## The website 

Livre Addict => https://www.livraddict.com/forum/viewcategory.php?id=4

This is a forum where everyone can publish reviews on books. 100% HTML / CSS.

Why this one ? Because we can access users data as age, sexe, localisation and amount of books read. Which is mandatory to create a match between a book and a 'persona'. And this is in French. 

## Structure of the website :

Level 1 :
* Main page of all genres : 1 page
* Fantasy, Fantastique et bit-lit: 16 pages
* Thriller, polar, aventure et horreur: 17 pages
* Jeunesse et Young Adult: 21 pages
* Contemporaine: 14 pages
* Classique, théâtre, poésie, nouvelles: 4 pages
* Science-Fiction: 5 pages
* Historique: 6 pages
* Romances: 8 pages
* Non-fiction: 4 pages
* BDs, Comics et Mangas: 7 pages
* Enfants (pour les plus petits et leurs parents): 3 pages

Total : 105

Level 2 : 
* ~30 books per page per genre

Total : 2 930 book url


Level 3 : Comment analysis
* Comments : ~95 000
* Page of Comments : ~9 500

Level 4 : profils
* Unique Profils : 77 000 inscris


## Workflow :
1) Get the first link
2) Get the pagination settings
3) Create a function that will read your soup and get the links for objects
4) Gather all the pages to get all the link to all objects
5) Create a function  that will read the soup of the object and collect all necessary information
6) Return your data into a df,csv,sql,db

=> Global time to scrap those 100 000 url is around 24 hours

## Reminders :
* Create a random sleep (1-5 s) for random number of pages (5-10)
* Use 'Task schuduler' to create task and run your script like twice a month 

## Libraries used :
* import requests as r
* from bs4 import BeautifulSoup
* import random
* import re
* import time
* import pandas as pd
* import numpy as np
* import pandas as pd
* import pymysql
* from sqlalchemy import create_engine
* from aylienapiclient import textapi
* import json
* from ibm_watson import ToneAnalyzerV3
* from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

## Challenges :
* Improve skills with Dict, pandas and SQL
* Deal with pages url and [..] in the pages indentation
* Deal with pages inside pages inside pages (4 levels)
* Deal with pages without pagination
* Uge amount of data
* Extract every post with only pseudo, profil link and all the text using Regex
* Deal with sentiment analysis and french content 
* Deal with APIs and Lib

## Hours :
- Jeudi : 5h
- Vendredi : 3h + 3h (end of all the scrapping code)+ (from 19h => put lst and dict into df)
- Samedi : 12h put df into mysql, use API AI to analyze text
- Dimanche : 2h debug 
Total : 25h

## Use Cases :
- As an author I want to write the perfect Thriller story for women, between 30-35 years old, living in IDF and that are reading less than 20 books / year
- As a marketing officer I want to push the last thriller story of my author to the right target


## Next steps :
- create a datapipeline to clean the df 
- provide a description of each columns of each df
- Create an UX interface for the author and the marketing officer with excel 
- Replace API by a Lib
- Use mac scheduler to run the script once a month
