from matplotlib import pyplot as plt
import itertools
from collections import Counter
file = open('text.txt','r',encoding='utf8').read().lower().replace('.','').replace(',','').replace('?','').split() #lexo filen dhe heq hapesirat etj
fjalet = Counter(file) #numero fjalet
counter_to_dictionary = dict(fjalet) #kthe ne dictionary
fjalet_me_te_perseritura =dict(sorted(counter_to_dictionary.items(), key=lambda item: item[1],reverse=True)) #order DESC
fjalet_me_te_perseritura = dict(itertools.islice(fjalet_me_te_perseritura.items(), 15)) #merr 15 elementet e para

count = fjalet_me_te_perseritura[(list(fjalet_me_te_perseritura.keys())[0])] #merr numrin e fjaleve me te perseritura
# print (count)
# print (fjalet_me_te_perseritura)
plt.yticks([5 * i for i in range(count+1)]) #boshti x me rritje per 5
plt.bar(fjalet_me_te_perseritura.keys(), fjalet_me_te_perseritura.values()) #vizualizo
plt.title("Fjalët më të shpeshta")
plt.ylabel("Numri i përseritjeve")
plt.xlabel("Fjalët")
plt.show()
