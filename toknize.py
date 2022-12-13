from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
stop_words.remove('in')
# todo the first modification I user here to instead of on
stop_words.remove('to')
stop_words.remove('where')


def tokenizer(doc):
    tokenized_documents = word_tokenize(doc)
    terms = []
    for word in tokenized_documents:
        if word not in stop_words:
            terms.append(word)
    return terms
