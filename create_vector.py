import os

from function import truncate_file_keywords, extract_key_words, read_pdf, read_file_key_words_final, write_keyword

# variable

direname = "Buffer-in/"
# direname = "base_keywords/"
filenames = os.listdir(direname)

file_bag_of_words = "output/bag_of_words.csv"
file_vector = "output/vector.csv"
truncate_file_keywords(file_bag_of_words)
truncate_file_keywords(file_vector)

header = ["fichier", "nb de mot ", "la liste des mots dans le fichier ", "\n"]
write_keyword(header, file_bag_of_words)

header = ["fichier ", "somme du vecteur ", "vecteur associe", "\n"]
write_keyword(header, file_vector)

vectors = dict()

for filename in filenames:
    text = read_pdf(direname + filename)
    keywords = extract_key_words(text)
    vectors[filename] = keywords
    line = [filename, str(len(keywords)), ';'.join(keywords), "\n"]
    write_keyword(line, file_bag_of_words)

# lire le fichier des mot cles

file_keywords = "output/dataframe.csv"
keywords = read_file_key_words_final(file_keywords)
# keywords=['Plateforme']
keywords = [item.lower() for item in keywords]

# print(keywords)
# print(len(keywords))
# print(vectors)
output = "output/dupllicat.csv"
truncate_file_keywords(output)
header = ["nombre de duplicat", "la liste des documents simulaires", "\n"]
write_keyword(header, output)
vectors_numerique = dict()

for cle, value in vectors.items():
    vector = [0] * len(keywords)
    for i in range(len(keywords)):
        vector[i] = value.count(keywords[i])

    if sum(vector) > 0:
        vectors_numerique[cle] = vector
        vector_str = [str(int) for int in vector]
        line = [cle, str(sum(vector)), ';'.join(vector_str), "\n"]
        write_keyword(line, file_vector)

# write_keyword(vectors_numerique.values(), output)
# print(vectors_numerique)
# print(len(vectors_numerique.keys()))


for cle, value in vectors_numerique.items():

    filenames_dupplicat = [cle2 for cle2, value2 in vectors_numerique.items() if value == value2]

    if len(filenames_dupplicat) > 1:
        line = [str(len(filenames_dupplicat)), ';'.join(filenames_dupplicat), "\n"]
        write_keyword(line, output)



