import csv
import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

#input_file = open('joe biden.csv')
# poll_data = pd.read_csv('biden.csv')

poll_data_list = []
candidate_list = []
no_tweets_list = []

total_tweets = 0

for files in glob.glob("data/*.csv"):
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
plt.pie(no_tweets_list, labels=candidate_list, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

from textblob import TextBlob

score = 0
positive_threshold = 0
negative_threshold = 0
pos_count = 0 
pos_sum = 0
neg_count = 0
neg_sum = 0

for str in poll_data_list[0]['text']:
    blob = TextBlob(str)
    blob.tags
    blob.noun_phrases  
    score += blob.sentiment.polarity
    #print(blob.sentiment.polarity)
    if (blob.sentiment.polarity >= positive_threshold):
        pos_count += 1
    if (blob.sentiment.polarity <= negative_threshold):
        neg_count += 1

    if (blob.sentiment.polarity >= 0):
        pos_sum += blob.sentiment.polarity
    else:
        neg_sum += blob.sentiment.polarity

pos_count_score = float(pos_count)/(pos_count+neg_count)
neg_count_score = float(neg_count)/(pos_count+neg_count)

pos_sum_score = float(pos_sum)/(pos_sum+abs(neg_sum))
neg_sum_score = float(abs(neg_sum))/(pos_sum+abs(neg_sum))

print('Polarity sum:', score)
print('Positive sum:', pos_sum_score)
print('Negative sum:', neg_sum_score)
print('Positive score:', pos_count_score)
print('Negative score:', neg_count_score)


blob.translate(to="es")
