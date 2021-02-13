import os

from extract_key_from_pdf import read_pdf, extract_key_words, write_keyword, truncate_file_keywords
from statistique import read_file_key_words_final
direname = "Buffer-in/"
#direname = "base_keywords/"
filenames = os.listdir(direname)
vectors = dict()

for filename in filenames:
    text = read_pdf(direname + filename)
    keywords = extract_key_words(direname + filename)
    vectors[filename] = keywords

# lire le fichier des mot cles

file_keywords = "output/dataframe.csv"
keywords = read_file_key_words_final(file_keywords)
#keywords=['Plateforme']
keywords=[item.lower() for item in keywords]

# print(keywords)
# print(len(keywords))
# print(vectors)
output = "output/dupllicat.csv"
truncate_file_keywords(output)

vectors_numerique = dict()

for cle, value in vectors.items():
    vector = [0] * len(keywords)

    for i in range(len(keywords)):
        if keywords[i] in value:
            vector[i] = 1

    vectors_numerique[cle] = vector

#write_keyword(vectors_numerique.values(), output)
# print(vectors_numerique)
# print(len(vectors_numerique.keys()))
for cle, value in vectors_numerique.items():

    filenames_dupplicat = [cle2 for cle2, value2 in vectors_numerique.items() if value == value2]
    # print(filenames_dupplicat)
    if len(filenames_dupplicat) > 1:
        write_keyword([" debut  ",cle,str(len(filenames_dupplicat)),"\n"], output)
        write_keyword(filenames_dupplicat, output)
        write_keyword(["\n"], output)
