import os
import random

import pandas as pd
import numpy as np
import re
from function import truncate_file_keywords, read_pdf, extract_key_words, read_file_key_words, write_keyword_by_line

# variable

nb = 200
direname = "Buffer-in/"
# direname = "base_keywords/"

filenames = os.listdir(direname)

nb_dco = 100
file_name_output = "output/keywords.csv"
rand = random.sample(filenames, nb_dco)


def count_words(file_name, file_name_df):
    words = read_file_key_words(file_name)

    text = ",".join(words)

    keywords = re.findall(r'[a-zA-Z]\w+', text)
    len(keywords)

    write_dataframe(keywords, text, file_name_df)


def write_dataframe(keywords, text, file_name_df):
    df = pd.DataFrame(list(set(keywords)), columns=['keywords'])

    df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x, text)[0])
    df['tf'] = df['keywords'].apply(lambda x: weightage(x, text)[1])
    df['idf'] = df['keywords'].apply(lambda x: weightage(x, text)[2])
    df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x, text)[3])

    df = df.sort_values('tf_idf', ascending=False)
    df.to_csv(file_name_df)
    df.head(25)
    print(df)


def weightage(word, text):
    word_list = re.findall(word, text)
    number_of_times_word_appeared = len(word_list)
    tf = number_of_times_word_appeared / float(len(text))
    idf = np.log(nb / float(number_of_times_word_appeared))
    tf_idf = tf * idf
    return number_of_times_word_appeared, tf, idf, tf_idf


# function.py main


truncate_file_keywords(file_name_output)

for filename in rand:
    if "pdf" in filename:
        text = read_pdf(direname + filename)
        keywords = extract_key_words(text)
        write_keyword_by_line(keywords, file_name_output)

count_words(file_name_output, 'output/dataframe.csv')
