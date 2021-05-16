from collections import Counter
import json
file = open('text1.txt', 'r').read() #leximi i file
counter = Counter(file.lower().split()) #ndarja e fjaleve
counter_dict = {i : counter[i] for i in counter} #konvertimi ne dictionary
counter_json = json.dumps(counter_dict) #konvertimi ne json
with open('json.json', 'w') as outfile:
    json.dump(counter_json, outfile) #shkruarja ne file
