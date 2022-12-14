import os

# from nltk import word_tokenize,sent_tokenize
#
# from nltk import word_tokenize,sent_tokenize
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
from natsort import natsorted
from toknize import tokenizer


# it will give me all the files names
files_names = natsorted(os.listdir('files'))
terms_of_documents = []

for file in files_names:
    with open(f'files/{file}', 'r') as f:
        document = f.read()
        print(document)
    terms = tokenizer(document)
    terms_of_documents.append(terms)
print(terms_of_documents)