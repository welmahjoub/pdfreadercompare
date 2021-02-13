import pandas as pd
import numpy as np
import PyPDF2
import textract
import re
from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from tika import parser

import string
import csv

nb=200

def read_file_key_words_final(file_name):
    with open(file_name, 'r',encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        keywords = []
        for row in spamreader:
            keywords.append(row[1])

        return keywords[2:]


def read_file_key_words(file_name):
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
    return Lines


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

    df = df.sort_values('idf', ascending=False)
    df.to_csv(file_name_df)
    df.head(25)
    print(df)


def weightage(word, text, number_of_documents=10):
    word_list = re.findall(word, text)
    number_of_times_word_appeared = len(word_list)
    tf = number_of_times_word_appeared / float(len(text))
    idf = np.log(number_of_documents / float(number_of_times_word_appeared))
    tf_idf = tf * idf
    return number_of_times_word_appeared, tf, idf, tf_idf
