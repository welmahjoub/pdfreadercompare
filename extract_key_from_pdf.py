import re
from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from tika import parser
import string


def extract_key_words(file_name,file_name_output):
    text = read_pdf(file_name)
    tokens = word_tokenize(text)
    punctuations = punctuations_french()
    stop_words = stop_words_french()

    keywords = [word for word in tokens if word not in stop_words and word not in punctuations]

    print(keywords)
    text2 = ",".join(keywords)

    keywords = re.findall(r'[a-zA-Z]\w+', text2)
    len(keywords)
    write_keyword(keywords, file_name_output)


def write_keyword(keywords, file_name_output):
    with open(file_name_output, 'a') as f:
        f.write('\n'.join(keywords))


def read_pdf(file_name):
    rawText = parser.from_file(file_name)
    rawList = rawText['content'].splitlines()
    rawList = [text.lower() for text in rawList if len(text)]
    text = ",".join(rawList)

    return text


def stop_words_french():
    french = get_stop_words('french')
    english = get_stop_words('english')
    return [*french, *english]


def punctuations_french():
    return string.punctuation


def truncate_file_keywords(filename):
    f = open(filename, 'w')
    f.close()




