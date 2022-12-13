from ir import terms_of_documents

# todo I comment all of that and will bring this list fro ir.py
# documents = [
#     ['antony', 'brutus', 'caeser', 'cleopatra', 'mercy', 'worser'],
#     ['antony', 'brutus', 'caeser', 'calpurnia'],
#     ['mercy', 'worser'], ['brutus', 'caeser', 'mercy', 'worser'],
#     ['caeser', 'mercy', 'worser'],
#     ['antony', 'caeser', 'mercy'],
#     ['angels', 'fools', 'fear', 'in', 'rush', 'tread', 'where'],
#     ['angels', 'fools', 'fear', 'in', 'rush', 'tread', 'where'],
#     ['angels', 'fools', 'in', 'rush', 'tread', 'where'],
#     ['fools', 'fear', 'in', 'rush', 'tread', 'where']]

document_num = 1
positional_index = {}

for document_terms in terms_of_documents:
    for position, term in enumerate(document_terms):

        if term in positional_index:
            # todo I add +1 here it was = 1
            positional_index[term][0] = positional_index[term][0] + 1
            # print(positional_index)
            if document_num in positional_index[term][1]:  # that will return the keys
                positional_index[term][1][document_num].append(position)

            else:
                positional_index[term][1][document_num] = [position]

        else:
            # {'antony':[]}
            positional_index[term] = []

            positional_index[term].append(1)

            positional_index[term].append({})

            positional_index[term][1][document_num] = [position]

    document_num += 1
print(positional_index)
