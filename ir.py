import os

from nltk import word_tokenize,sent_tokenize

from nltk import word_tokenize,sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from natsort import natsorted
stop_words =stopwords.words('english')
stop_words.remove('in')
stop_words.remove('on')
stop_words.remove('where')

files_name = natsorted(os.listdir('files'))

document_of_terms = []

for files in files_name:
    with open(f'files/{files}', 'r') as f:
        document = f.read()
    tokenized_documents = word_tokenize(document)  
    terms = []
    for word in tokenized_documents:
        if word not in stop_words:
            terms.append(word)
    document_of_terms.append(terms)
print(document_of_terms)