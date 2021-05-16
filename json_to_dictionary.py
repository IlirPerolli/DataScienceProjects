import json

dict = {'name':'Ilir', 'surname':'Perolli', 'age':21} #kriji i dictionary
dict_to_json = json.dumps(dict) #konvertimi ne json
with open('json_file.json', 'w') as outfile:
    json.dump(dict_to_json, outfile) #shkruarja ne file

with open('json_file.json') as f:
    data = json.load(f) #leximi i json files

person_dict = json.loads(data) #konvertimi ne dictionary
print(person_dict['name']) #leximi
