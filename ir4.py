import pandas as pd
import math
import numpy as np

# documents= [
#     ['antony', 'brutus', 'caeser', 'cleopatra', 'mercy', 'worser'],
#     ['antony', 'brutus', 'caeser', 'calpurnia'],
#     ['mercy', 'worser'], ['brutus', 'caeser', 'mercy', 'worser'],
#     ['caeser', 'mercy', 'worser'],
#     ['antony', 'caeser', 'mercy'],
#     ['angels', 'fools', 'fear', 'in', 'rush', 'tread', 'where'],
#     ['angels', 'fools', 'fear', 'in', 'rush', 'tread', 'where'],
#     ['angels', 'fools', 'in', 'rush', 'tread', 'where'],
#     ['fools', 'fear', 'in', 'rush', 'tread', 'where']
# ]

from ir import terms_of_documents as documents

all_words = []
for doc in documents:
    for word in doc:
        all_words.append(word)


# todo remove these prints later
# print(dict.fromkeys(all_words, 0))
# print(all_words)


def get_term_freq(doc):
    words_found = dict.fromkeys(all_words, 0)

    for word in doc:
        words_found[word] += 1
    return words_found


term_freq = pd.DataFrame(get_term_freq(documents[0]).values(), index=get_term_freq(documents[0]).keys())

# I write here 1 because we did 0 earlier in the code
for i in range(1, len(documents)):
    term_freq[i] = get_term_freq(documents[i]).values()
term_freq.columns = ['doc' + str(i) for i in range(1, 11)]
# it's the term frequency table
print('========================================================================')
print("Term Frequency table")
print(' ')
print(term_freq)


def get_weighted_term_freq(x):
    if x > 0:
        # todo I change the base here to 10
        return math.log(x, 10) + 1
    return 0


for i in range(1, len(documents) + 1):
    # .apply make him take every index value here and apply the function on it
    term_freq['doc' + str(i)] = term_freq['doc' + str(i)].apply(get_weighted_term_freq)

# it's the term frequency table after applying 1 + log(term_frequency) equation
print('========================================================================')
print("Term Frequency after applying 1 + log(tf)")
print(' ')
print(term_freq)




idf = pd.DataFrame(columns=['df', 'idf'])

for i in range(len(term_freq)):
    # It will get the number of documents that contains the term
    frequency = term_freq.iloc[i].values.sum()
    idf.loc[i, 'df'] = int(frequency)
    idf.loc[i, 'idf'] = math.log(10 / float(frequency), 10)

idf.index = term_freq.index
# here he will print the df and idf for each term
print('========================================================================')
print("document frequency && inverse document frequency")
print(' ')
print(idf)

term_freq_inve_doc_freq = term_freq.multiply(idf['idf'], axis=0)
print('========================================================================')
print("tf_idf")
print(' ')
print(term_freq_inve_doc_freq)

document_length = pd.DataFrame()


def get_docs_length(col):
    return np.sqrt(term_freq_inve_doc_freq[col].apply(lambda x: x ** 2).sum())


for column in term_freq_inve_doc_freq.columns:
    document_length.loc[0, column + '_len'] = get_docs_length(column)
print('========================================================================')
print("document length")
print(' ')
print(document_length.T)
normalized_tf_idf = pd.DataFrame()


def get_normalized(col, x):
    if document_length[col + '_len'].values[0] != 0:
        return x / document_length[col + '_len'].values[0]
    return 0


for column in term_freq_inve_doc_freq.columns:
    normalized_tf_idf[column] = term_freq_inve_doc_freq[column].apply(lambda x: get_normalized(column, x))
print('========================================================================')
print("Normalized tf_idf")
print(' ')
print(normalized_tf_idf)
