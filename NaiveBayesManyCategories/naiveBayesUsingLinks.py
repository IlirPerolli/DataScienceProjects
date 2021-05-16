from bs4 import BeautifulSoup
import re
import requests
import naiveBayesClassifier
import math
from naiveBayesClassifier import Message
from naiveBayesClassifier import NaiveBayesClassifier
import numpy as np
while True:

    sports = []
    politics = []
    economy = []
    health = []
    directories = ['sports','politics', 'economy', 'health']
    category_arrays = [sports,politics, economy, health]

    for count, i in enumerate(category_arrays):
        file = open(directories[count]+'/file1.txt', encoding='utf8').read().lower().split()
        for j in file:
            if len(j)<4:
                continue
            i.append(j)
    # print (economy)

    sports =list(set(sports)-set(politics)-set(economy)-set(health))
    politics =list(set(politics)-set(economy)-set(sports)-set(health))
    economy =list(set(economy)-set(sports)-set(politics)-set(health))
    health = list(set(health)-set(economy)-set(sports)-set(politics))

    sport_messages = [
        Message(str(i), is_spam=True) for i in sports]
    for i in politics:
        sport_messages.append(Message(str(i), is_spam=False))
    for i in economy:
        sport_messages.append(Message(str(i), is_spam=False))
    for i in health:
        sport_messages.append(Message(str(i), is_spam=False))
    # print (sport_messages)

    politics_messages = [
        Message(str(i), is_spam=True) for i in politics]
    for i in sports:
        politics_messages.append(Message(str(i), is_spam=False))
    for i in economy:
        politics_messages.append(Message(str(i), is_spam=False))
    for i in health:
        politics_messages.append(Message(str(i), is_spam=False))

    economy_messages = [
        Message(str(i), is_spam=True) for i in economy]
    for i in politics:
        economy_messages.append(Message(str(i), is_spam=False))
    for i in sports:
        economy_messages.append(Message(str(i), is_spam=False))
    for i in health:
        economy_messages.append(Message(str(i), is_spam=False))

    health_messages = [
        Message(str(i), is_spam=True) for i in health]
    for i in sports:
        health_messages.append(Message(str(i), is_spam=False))
    for i in economy:
        health_messages.append(Message(str(i), is_spam=False))
    for i in politics:
        health_messages.append(Message(str(i), is_spam=False))
    # print (sport_messages)


    sport = NaiveBayesClassifier(k=0.5)
    sport.train(sport_messages)
    politics = NaiveBayesClassifier(k=0.5)
    politics.train(politics_messages)
    economy = NaiveBayesClassifier(k=0.5)
    economy.train(economy_messages)
    health = NaiveBayesClassifier(k=0.5)
    health.train(health_messages)

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
    text_to_save = str(text)
    text = str(text[4:500])
    sport_result = sport.predict(text)
    politics_result = politics.predict(text)
    economy_result = economy.predict(text)
    health_result = health.predict(text)

    results = {'sport':sport_result,'politike':politics_result, 'ekonomi':economy_result, 'shendetesi':health_result}
    max_value = max(sport.predict(text),politics.predict(text),economy.predict(text), health.predict(text))

    print (results)

    for count, category in enumerate(results.keys()):
        if results[category] == max_value and max_value>0:
            print ("Lajmi eshte i kategorise "+category+" me saktesi: "+str(max_value))
            directory_count = count
            break


    # print (results)
    if (max_value>0.9 and max_value <1):
        choice = input("Deshironi te fusni ne file per te permiresuar detektimin? (Y | N): ")
        if choice == 'Y' or choice == 'y':
            file_to_write = open(directories[directory_count]+'/file1.txt','a', encoding='utf8')
            temp_file = open(directories[directory_count]+'/file1.txt', encoding='utf8').read().lower()
            if text not in temp_file:
                file_to_write.write("\n"+str(text_to_save))
            file_to_write.close()
            print ("Lajmi u vendos ne file me sukses")
        if(choice == 'N' or choice == 'n'):
            choice = int(input("Ciles kategori i takon? (1-Sport, 2-Politike, 3-Ekonomi, 4-Shendetesi): "))
            if (choice>=1 and choice<=4):
                file_to_write = open(directories[choice-1]+'/file1.txt','a', encoding='utf8')
                temp_file = open(directories[choice-1]+'/file1.txt', encoding='utf8').read().lower()
                if text not in temp_file:
                    file_to_write.write("\n"+str(text_to_save))
                file_to_write.close()
                print ("Lajmi u vendos ne file me sukses. Ju faleminderit per kontributin!")
    elif (max_value==0):
        choice = int(input("Ciles kategori i takon? (1-Sport, 2-Politike, 3-Ekonomi, 4-Shendetesi): "))
        if (choice>=1 and choice<=4):
            file_to_write = open(directories[choice-1]+'/file1.txt','a', encoding='utf8')
            temp_file = open(directories[choice-1]+'/file1.txt', encoding='utf8').read().lower()
            if text not in temp_file:
                file_to_write.write("\n"+str(text_to_save))
            file_to_write.close()
            print ("Lajmi u vendos ne file me sukses. Ju faleminderit per kontributin!")

