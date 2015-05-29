# accept text from sample.txt
# create a dictionary
# collect top 20 words used
# reverse top 20 words
# print top 20 words
# store results in an outside file
import re

with open ('/Users/lancerogers/homework/word_frequency/word-frequency/sample.txt','r') as file:
    file_str = file.read()

    def sample(file_str):
        h_dict = {}
        #print(file_str)
        for line in file_str.split():
            #print(line)
            for words in line.split():

                words = re.sub(r'[^A-Za-z\s]',"", words.lower())
                try:
                    words != ''
                except:
                    pass
                #print(words)
                # words = re.sub('[" "]', '', words.lower())
            if words in h_dict:
                h_dict[words] = h_dict[words] + 1
            else:
                h_dict[words] = 1

        return h_dict



h_dict = sample(file_str)
print(h_dict)
