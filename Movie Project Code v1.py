import pandas as pd
import numpy as np
import re
import string
from nltk.corpus import stopwords

# Establish column names for the data frame
colname = ['critic_rating_val', 'critic_rating_num', 'user_rating', 'user_rating_num', 'mpaa_rating', 'genres', 'movie_date', 'movie_name', 'description', 'current_url']

# Read in the movie data
meta = pd.read_table('C:/Users/Jordan/Documents/School/University of Virginia/Summer 2016/CS5010 - Programming and Systems for Data Analysis/Project/movie_details copy.txt', sep='|', names=colname)

# Read in dates into 'YYYY-MM-DD' format with no timestamps
meta['movie_date'] = pd.to_datetime(meta['movie_date'], errors='coerce').dt.date

# Strip out punctuation from description
meta['c_desc'] = meta['description'].str.replace('[^\w\s]','')

set(list(meta['mpaa_rating']))

# Remove user ratings that are "Unknown" or "tbd"
# Remove mpaa_ratings that are "Unknown", "Not Rated", or TV-related
# Remove 
meta_sub = meta[meta["user_rating"] != "Unknown"]
meta_sub = meta_sub[meta_sub["user_rating"] != "tbd"]
meta_sub = meta_sub[meta_sub["mpaa_rating"] != "Unknown"]
meta_sub = meta_sub[meta_sub["mpaa_rating"] != "Not Rated"]
meta_sub = meta_sub[meta_sub["mpaa_rating"].str.contains("TV") == False]

# Change numeric columns to integer values

# combine genres
# combine ratings
# comedy, doc, drama, aaction, romance, mystery/thriller, animation, horror