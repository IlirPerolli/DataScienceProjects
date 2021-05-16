from bs4 import BeautifulSoup
import re
import requests


from typing import Set
import re
import naiveBayesClassifier
import math
from naiveBayesClassifier import Message
from naiveBayesClassifier import NaiveBayesClassifier
import numpy as np
while True:

    sports = []
    politics = []

    file1_sport = open('sports/file1.txt', encoding='utf8').read().lower().split()
    sports_array = file1_sport

    for i in sports_array:
        if len(i)<4:
            continue
        sports.append(i)
    file1_politics = open('politics/file1.txt', encoding='utf8').read().lower().split()

    politics_array=file1_politics
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

    url = input("Jepni linkun per te shikuar llojin e lajmit: ")
    html = requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    text = ""

    for item in soup.find('div', class_='article-heading').find_all('h1'):
        text += str(item)
    for item in soup.find('div', class_='article-body').find_all('p'):
        text += str(item)


    text = text.lower()
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
        file_sport = open('sports/file1.txt','a', encoding='utf8')
        if (sport.predict(text)>0.9):
            file1_sport = open('sports/file1.txt', encoding='utf8').read().lower()
            if text not in file1_sport:
                file_sport.write("\n"+str(text))

        file_sport.close()
    else:
        print ("Lajmi eshte i kategorise politike me saktesi: "+str(politics.predict(text)))
        file_politics = open('politics/file1.txt','a', encoding='utf8')
        if (politics.predict(text)>0.9):
            file1_politics = open('politics/file1.txt', encoding='utf8').read().lower()
            if text not in file1_politics:
                file_politics.write("\n"+str(text))
        file_politics.close()
    # print(sport.predict(text))
    # print(politics.predict(text))


