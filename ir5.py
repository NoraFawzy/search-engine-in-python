import pandas as pd
from ir3 import matched_docs, query as q
from process_query import query_processing
from ir4 import normalized_tf_idf

if matched_docs:
    query_terms_table = query_processing(q)
    matched_docs_table = pd.DataFrame(index=query_terms_table.index)
    print(f'matched docs {matched_docs}')
    for doc in matched_docs:
        # print(doc)
        # print(normalized_tf_idf['doc' + str(doc)])

        matched_docs_table['doc' + str(doc)] = normalized_tf_idf['doc' + str(doc)].multiply(
            query_terms_table['normalized'], axis=0)

    matched_docs_table.loc['sum'] = [matched_docs_table['doc' + str(doc)].sum() for doc in matched_docs]
    print('product ( query * matched docs)')
    print(matched_docs_table)
    # convert the sum row to dic so I can handle it better
    docs_scores = matched_docs_table.loc['sum'].to_dict() # {'doc1': 0.53, 'doc2': 0.57}
    # print cosine similarity of docs
    for doc in docs_scores:
        print(f'cosine similarity in (q, {doc}) = {docs_scores[doc]}')

    sorted_docs_score = dict(reversed(sorted(docs_scores.items(), key=lambda item: item[1])))
    print('returned docs :')
    for doc in sorted_docs_score:
        print(doc)
else:
    print('No matched docs')