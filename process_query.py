from toknize import tokenizer
from ir2 import positional_index
from ir4 import idf as df_idf, get_weighted_term_freq
import pandas as pd
import numpy as np


def query_processing(query):
    query_terms_list = tokenizer(query)
    table = pd.DataFrame(index=positional_index)
    table['query_terms'] = [1 if x in query_terms_list else 0 for x in list(positional_index)]
    print(table)
    query_terms = table.index[table['query_terms'] == 1].tolist()
    print(query_terms)
    query_terms_table = pd.DataFrame(index=query_terms)
    # getting term frequency
    query_terms_table['tf'] = [0] * len(query_terms)
    for term in query_terms_list:
        query_terms_table.loc[term, 'tf'] += 1
    # getting w_tf = 1 + log(tf)
    query_terms_table['w_tf'] = query_terms_table['tf'].apply(get_weighted_term_freq)

    # getting idf which is computed earlier
    query_terms_table['idf'] = df_idf.loc[query_terms_table.index.tolist(), 'idf']
    # getting tf_idf
    query_terms_table['tf*idf'] = query_terms_table['w_tf'].multiply(query_terms_table['idf'], axis=0)

    # getting query length
    query_length = np.sqrt(query_terms_table['tf*idf'].apply(lambda x: x ** 2).sum())

    # getting normalization
    query_terms_table['normalized'] = query_terms_table['tf*idf'].apply(lambda x: x / query_length)

    print(query_terms_table)
    print(f'query length = {query_length}')

    return query_terms_table

