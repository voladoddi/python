# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 03:21:29 2014

@author: voladoddi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns',50)

'''A series is a 1-D object similar to an array, list, or column in a table.
   Assigns labeled index to each item in a series.
   last element's number is length of series = N - 1'''
   
#create a series with an arbitrary list
s =pd.Series([7,'Heisenberg',3.14,-17877,'Happy eating'])
s
#specifying EXPLICIT indices
s1 =pd.Series([7,'Heisenberg',3.14,-17877,'Happy eating'],['p','o','j','a','v'])
s1

#converting a dictionary into series 
d = {'chicago':1000,'ny':1300,'portland':900,'san francisco':1100,'austin':450,'boston':'none'}
cities = pd.Series(d)
print cities

#make a list of cities having index value less than 1000 and then pass them onto 
#Series constructor
print cities[cities < 1000]

################################################################################
###############################################################################
''' A data frame is a tabular structure - rows & columns - DATABASE/SPEADSHEET
like.

Equivalent to R's "data.frame object.

Or : group of series objects sharing an index.'''

u_cols = ['user_id','age','sex','occupation','zip_code']
users = pd.read_csv('ml-100k/u.user',sep='|',names=u_cols)

r_cols = ['user_id','movie_id','rating','unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data',sep='\t',names=r_cols)

#the movies file contains columns indicating the movie's genres
#loading only 5 first columns using "usecols"
m_cols= ['movie_id','title','release_date','video_release_date','imdb_url']
movies =pd.read_csv('ml-100k/u.item',sep='|',names=m_cols,usecols=range(5))

movie_ratings = pd.merge(movies,ratings)
lens = pd.merge(movie_ratings,users)

most_rated = lens.groupby('title').size().order(ascending=False)[:25]
print most_rated

movie_stats = lens.groupby('title').agg({'rating':[np.size,np.mean]})
print movie_stats.head()

#sort by rating average (depending on whether they got atleast 100 ratings )
print movie_stats[movie_stats['rating'].size>=100].sort([('rating','mean')],ascending=False)[:10]


users.age.hist(bins=30)
plt.title("Distribution of Users' ages")
plt.ylabel('user count')
plt.xlabel('age')
plt.show()




