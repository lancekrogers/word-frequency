# accept text from sample.txt
# create a dictionary
# collect top 20 words used
# reverse top 20 words
# print top 20 words
# store results in an outside file

import re

with open ('/Users/lancerogers/homework/word_frequency/word-frequency/sample.txt','r') as file:
    file_str = file.read()
    # print(file_str)
    def word_frequency(file_str):
        h_dict = {}
        # print(file_str)
        words = re.sub(r'[^A-Za-z\s]',"", file_str).lower().split()
        for string in words:
            if string in h_dict:
                h_dict[string] = h_dict[string] + 1
            else:
                h_dict[string] = 1
        return h_dict

h_dict = word_frequency(file_str)
# print(h_dict)


# create a function that takes in a dictionary and returns the top 20
# occurances in that dictionary
headache = sorted(h_dict.items(), key = lambda x: x[1], reverse = True)
top_twenty = headache[:20]

def strip_list(top_twenty):
    for value in top_twenty:
        if value != None:
            tuple_str = value[0]
            tuple_int = value[1]
            print("{} {}".format(tuple_str, tuple_int))
            continue
        else:
            break
        return
strip_list(top_twenty)
