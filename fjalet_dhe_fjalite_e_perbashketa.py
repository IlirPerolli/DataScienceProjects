file1 = open('text1.txt', 'r').read().lower().replace('.','').replace(',','').replace('?','').split() #leximi i fjaleve
file2 = open('text2.txt', 'r').read().lower().replace('.','').replace('?','').replace(',','').split() #leximi i fjaleve
unique_words_of_file1 = (set(file1)) #krijimi i setave
unique_words_of_file2 = (set(file2)) #krijimi i setave
unique_words = unique_words_of_file1.intersection(unique_words_of_file2) #te perbashketat e setave
print ('Fjalet e ngjashme: ')
for i in unique_words:
    print(i, end=" ")
print ("")

print ("Fjalite e ngjashme:")

file1 = open('text1.txt', 'r').read().lower().replace('?','.').split('.') #leximi i fjaleve
file2 = open('text2.txt', 'r').read().lower().replace('?','.').split('.') #leximi i fjaleve

unique_sentence_of_file1 = (set(file1)) #krijimi i setave
unique_sentence_of_file2 = (set(file2)) #krijimi i setave
unique_sentence = (unique_sentence_of_file1.intersection(unique_sentence_of_file2)) #te perbashketat e setave
for i in (unique_sentence):
        print(i, end=" ")
print ("")