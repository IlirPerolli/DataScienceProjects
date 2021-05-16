from typing import Set
import re
import naiveBayesClassifier
import math
from naiveBayesClassifier import Message
from naiveBayesClassifier import NaiveBayesClassifier
import numpy as np

sports = []
politics = []

file1_sport = open('sports/file1.txt', encoding='utf8').read().lower().split()
file2_sport = open('sports/file2.txt', encoding='utf8').read().lower().split()
file3_sport = open('sports/file3.txt', encoding='utf8').read().lower().split()
file4_sport= open('sports/file4.txt', encoding='utf8').read().lower().split()
file5_sport = open('sports/file5.txt', encoding='utf8').read().lower().split()
sports_array=np.concatenate((file1_sport, file2_sport,file3_sport,file4_sport,file5_sport), axis=None)
for i in sports_array:
    if len(i)<4:
        continue
    sports.append(i)
file1_politics = open('politics/file1.txt', encoding='utf8').read().lower().split()
file2_politics = open('politics/file2.txt', encoding='utf8').read().lower().split()
file3_politics = open('politics/file3.txt', encoding='utf8').read().lower().split()
file4_politics= open('politics/file4.txt', encoding='utf8').read().lower().split()
file5_politics = open('politics/file5.txt', encoding='utf8').read().lower().split()
politics_array=np.concatenate((file1_politics, file2_politics,file3_politics,file4_politics,file5_politics), axis=None)
for i in politics_array:
    if len(i)<4:
        continue
    politics.append(i)
sports = list(set(sports))
politics = list(set(politics))

sports_list = np.setdiff1d(sports,politics)
politics_list = np.setdiff1d(politics,sports)
same_words = set(sports).intersection(set(politics))

sport_messages = [
            Message(str(i), is_spam=True) for i in sports_list]
for i in politics_list:
    sport_messages.append(Message(str(i), is_spam=False))
# print (sport_messages)

sport = NaiveBayesClassifier(k=0.5)
sport.train(sport_messages)

politics_messages = [
    Message(str(i), is_spam=True) for i in politics_list]
for i in sports_list:
    politics_messages.append(Message(str(i), is_spam=False))
# print (sport_messages)

politics = NaiveBayesClassifier(k=0.5)
politics.train(politics_messages)

file_to_check = open('news_to_check.txt', encoding='utf8').read().lower()


text = file_to_check
probs_if_spam = [
    (1 + 0.5) / (1 + 2 * 0.5),
    1 - (0 + 0.5) / (1 + 2 * 0.5),
    1 - (1 + 0.5) / (1 + 2 * 0.5),
    (0 + 0.5) / (1 + 2 * 0.5)
]

probs_if_ham = [
(0 + 0.5) / (2 + 2 * 0.5),
1 - (2 + 0.5) / (2 + 2 * 0.5),
1 - (1 + 0.5) / (2 + 2 * 0.5),
(1 + 0.5) / (2 + 2 * 0.5),
]
p_if_spam = math.exp(sum(math.log(p) for p in probs_if_spam))
p_if_ham = math.exp(sum(math.log(p) for p in probs_if_ham))

if (sport.predict(text) > politics.predict(text)):
    print ("Lajmi eshte i kategorise sport me saktesi: "+str(sport.predict(text)))
else:
    print ("Lajmi eshte i kategorise politike me saktesi: "+str(politics.predict(text)))
# print(sport.predict(text))
# print(politics.predict(text))


