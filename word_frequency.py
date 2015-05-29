# accept text from sample.txt
# create a dictionary
# collect top 20 words used
# reverse top 20 words
# print top 20 words
# store results in an outside file
import re

with open ('/Users/lancerogers/homework/word_frequency/word-frequency/sample.txt','r') as file:
    file_str = file.read()
    #print(file_str)
    def word_frequency(file_str):
        h_dict = {}
        #print(file_str)
        #for line in file_str.split():
            #print(line)
            #for words in line.split():

        words = re.sub(r'[^A-Za-z\s]',"", file_str).lower().split()
        for string in words:
            if string in h_dict:
                h_dict[string] = h_dict[string] + 1
            else:
                h_dict[string] = 1
        return h_dict

h_dict = word_frequency(file_str)
print(h_dict)
