#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:15:28 2019

@author: farihamoomtaheen
"""

import twitter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob
import csv
import glob
import os

poll_data_list = []
candidate_list = []
no_tweets_list = []

total_tweets = 0

for files in glob.glob("*.csv"):
    print(files)
    poll_data = pd.read_csv(files)
    poll_data_list.append(poll_data)
    candidate_list.append(os.path.splitext(files)[0])
    no_tweets_list.append(len(poll_data))
    total_tweets += len(poll_data)

plt.bar(candidate_list, no_tweets_list, align='center', alpha=0.5)
plt.xlabel('Candidate name')
plt.ylabel('Number of tweets')
plt.show()

colors = ['yellow', 'red', 'orange', 'green', 'blue', 'cyan', 'purple']
plt.pie(no_tweets_list, labels=candidate_list, colors = colors, autopct='%1.1f%%', shadow=True, startangle=140)



pos_count_list = []
cand_user_list = []
cand_user_count = []

for cand in poll_data_list:
    score = 0
    positive_threshold = 0
    negative_threshold = 0
    pos_count = 0 
    pos_sum = 0
    neg_count = 0
    neg_sum = 0
    users = []
    
    it = 0
    for str in cand['text']:
        blob = TextBlob(str)
        blob.tags
        blob.noun_phrases  
        score += blob.sentiment.polarity
        #print(blob.sentiment.polarity)
        if (blob.sentiment.polarity >= positive_threshold):
            pos_count += 1
            users.append(cand['username'][it])
        if (blob.sentiment.polarity <= negative_threshold):
            neg_count += 1
    
        if (blob.sentiment.polarity >= 0):
            pos_sum += blob.sentiment.polarity
        else:
            neg_sum += blob.sentiment.polarity
        it = it + 1
    
    
    pos_count_score = float(pos_count)/(pos_count+neg_count)
    neg_count_score = float(neg_count)/(pos_count+neg_count)
    
    pos_sum_score = float(pos_sum)/(pos_sum+abs(neg_sum))
    neg_sum_score = float(abs(neg_sum))/(pos_sum+abs(neg_sum))
    
#    print('Polarity sum:', score)
#    print('Positive sum:', pos_sum_score)
#    print('Negative sum:', neg_sum_score)
#    print('Positive score:', pos_count_score)
#    print('Negative score:', neg_count_score)
#    print("\n")
    
    pos_count_list.append(pos_count)
    cand_user_list.append(users)


plt.bar(candidate_list, pos_count_list, align='center', alpha=0.5)
plt.xlabel('Candidate name')
plt.ylabel('Number of positive tweets')
plt.show()

poll_list = [15, 9, 4, 29, 20, 2, 5]
plt.bar(candidate_list, poll_list, align='center', alpha=0.5)
plt.xlabel('Candidate name')
plt.ylabel('Number of LVs')
plt.show()


#search_results = twitter_api.search.tweets(q=q, count=count)


import twitter
import json

CONSUMER_KEY = ''
CONSUMER_SECRET =''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)
user_follower_count = []
print(username_list[:10])
for u in username_list:
    try:
        #print(u)
        result = twitter_api.users.lookup(screen_name = u)
        #user_follwer_count= result
        #print(result[0]['followers_count'])
        user_follower_count.append(result[0]['followers_count'])
    except:
        user_follower_count.append(0)
    
dftry = pd.read_csv("output_got.csv")
print(cand_user_list[0])

#for cand_user in cand_user_list:


user_follower_count = []

for u in cand_user_list[4]:
    try:
        print(u)
        result = twitter_api.users.lookup(screen_name = u)
        user_follower_count.append(result[0]['followers_count'])
        print(result[0]['followers_count'])
    except:
        user_follower_count.append(0)
        
print("COUNT")
print(user_follower_count)
print(sum(user_follower_count))
cand_user_count.append(sum(user_follower_count))

#0 = 3598737
#1 = 2945725
#2 = 784432
#3 = 13128807
#4 = 1835577
#5 = 199643
#6 = 3468228

follower_count_list = [3598737, 2945725, 784432, 13128807, 1835577, 199643, 3468228]

    
plt.bar(candidate_list, follower_count_list, align='center', alpha=0.5)
plt.xlabel('Candidate name')
plt.ylabel('Number of followers exposed')
plt.show()

