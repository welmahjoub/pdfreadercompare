import os
from extract_key_from_pdf import extract_key_words, truncate_file_keywords, write_keyword, read_pdf
from statistique import count_words

direname = "Buffer-in/"
#direname = "base_keywords/"
filenames = os.listdir(direname)
# print(filenames[1:100])


file_name_output = "output/keywords.csv"

truncate_file_keywords(file_name_output)

for filename in filenames[1:100]:
    if "pdf" in filename:
        text = read_pdf(direname+filename)
        keywords = extract_key_words(direname+filename)
        write_keyword(keywords, file_name_output)


count_words(file_name_output, 'output/dataframe.csv')


