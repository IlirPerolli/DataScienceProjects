import csv
import json
fjalet = {'ilir':21, 'blerim':50}
dict_to_json = json.dumps(fjalet)
with open('file.txt') as f:
    # json.dump(fjalet,f)
    # tab = csv.reader(f,delimiter='\t')
    # data = tab[0]
    # process(data)
    print (f.read().lower().split())

# for i in fjalet:
#     print (i + str(fjalet[i]))