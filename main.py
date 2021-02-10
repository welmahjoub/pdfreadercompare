import os
from extract_key_from_pdf import extract_key_words, truncate_file_keywords
from statistique import count_words

filenames = os.listdir("Buffer-in/")
print(filenames)

file_name_output = "keywords.csv"

truncate_file_keywords(file_name_output)

for filename in filenames:
    extract_key_words("Buffer-in/"+filename, file_name_output)


count_words(file_name_output)


