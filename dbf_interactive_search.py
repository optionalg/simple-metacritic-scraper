# coding: utf-8
# import data scraped in metascraper.ipynb
import pandas as pd
import numpy as np
import re
import string
from nltk.corpus import stopwords

colname = ['critic_rating_val', 'critic_rating_num', 'user_rating', 'user_rating_num', 'mpaa_rating', 'genres', 'movie_date', 'movie_name', 'description', 'current_url']
meta = pd.read_table('/Users/bradyfowler/Documents/Summer Session/CS 5010/metacritic/movie_details.txt', sep='|', names=colname)
meta['movie_date'] = pd.to_datetime(meta['movie_date'], errors='coerce')
meta['c_desc'] = meta['description'].str.replace('[^\w\s]','')

happy = 'y'
while (happy=='y'):
    mon = input("What month were you born? ")
    day = input("What day were you born? ")
    matches = meta.loc[(meta['movie_date'].dt.month==int(mon)) & (meta['movie_date'].dt.day==int(day))]
    matches = list(matches['movie_name'])
    if len(matches) > 0:
        print('You may enjoy these movies that came out on your birthday:')
        [print(x) for x in matches]
    else:
        print('There are no movies in the dataset on that date!')
    happy = input('Would you like to try a different date? (y/n)')