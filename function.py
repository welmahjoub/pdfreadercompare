from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from tika import parser
import string
import csv
import re


# variable
nb=200


def extract_key_words(text):
    tokens = word_tokenize(text)
    res = ",".join(tokens)
    keywords = re.findall(r'[a-zA-Z]\w+', res)

    # print("token :")
    # print(tokens)
    punctuations = punctuations_french()
    stop_words_fren = stop_words_french()
    stop_words_engl = stop_words_english()

    # tokens=text.split(",")
    keywords = [word.lower() for word in keywords]
    keywords = [word for word in keywords if word not in stop_words_fren]
    keywords = [word for word in keywords if word not in stop_words_engl]
    keywords = [word for word in keywords if word not in punctuations]

    print(keywords)
    return keywords


def write_keyword(keywords, file_name_output):
    with open(file_name_output, 'a', encoding='utf-8') as f:
        f.write(','.join(keywords))


def write_keyword_by_line(keywords, file_name_output):
    with open(file_name_output, 'a', encoding='utf-8') as f:
        f.write('\n'.join(keywords))


def read_pdf(file_name):
    rawText = parser.from_file(file_name)

    if rawText['content']:
        rawList = rawText['content'].splitlines()
        rawList = [text.lower() for text in rawList if len(text)]
        # print("rawList: ")
        # print(rawList)
        text = ",".join(rawList)

        return text
    else:
        return ""


def stop_words_french():
    french = get_stop_words('french')

    return french


def stop_words_english():
    english = get_stop_words('english')
    return english


def punctuations_french():
    return string.punctuation


def truncate_file_keywords(filename):
    f = open(filename, 'w')
    f.close()

# lire fichier dataframe
def read_file_key_words_final(file_name):
    with open(file_name, 'r', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        keywords = []
        for row in spamreader:
            keywords.append(row[1])

        punctuations = punctuations_french()
        stop_words_f = stop_words_french()
        stop_words_e = stop_words_english()

        keywords = [word for word in keywords if
                    word not in stop_words_f and word not in stop_words_e and word not in punctuations]

        return keywords[2:nb]


def read_file_key_words(file_name):
    file1 = open(file_name, 'r', encoding="utf8")
    Lines = file1.readlines()
    return Lines

