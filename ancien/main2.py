
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from tika import parser

import string

filename= "../base_keywords/00001-Stage - DÃ©veloppement d'une solution HomeNetWorking.pdf"
rawText = parser.from_file(filename)

rawList = rawText['content'].splitlines()

tokens = word_tokenize(",".join(rawList))


punctuations = string.punctuation
# punctuations = ['(',')',';',':','[',']',',']
# punctuations.append()
stop_words = stopwords.words('english')
stop_words.append(stopwords.words('french'))

keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

print(keywords)

with open('../output/keywords.csv', 'w') as f:
  f.write('\n'.join(keywords))