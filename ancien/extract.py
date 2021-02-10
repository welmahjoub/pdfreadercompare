from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from tika import parser

import string


def write_keyword(keywords):
    with open('../keywords.csv', 'a') as f:
        f.write('\n'.join(keywords))


def extract(filename):
    rawText = parser.from_file(filename)
    rawList = rawText['content'].splitlines()

    tokens = word_tokenize(",".join(rawList))

    punctuations = punctuations_french()

    stop_words = stop_words_french()

    keywords = [word for word in tokens if word not in stop_words and word not in punctuations]
    write_keyword(keywords)


def stop_words_french():
    stop_words = stopwords.words('english')
    stop_words.append(stopwords.words('french'))
    return stop_words


def punctuations_french():
    return string.punctuation
