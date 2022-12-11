documents = [
    ['antony', 'brutus', 'caeser', 'cleopatra', 'mercy', 'worser'], 
    ['antony', 'brutus', 'caeser', 'calpurnia'], 
    ['mercy', 'worser'], ['brutus', 'caeser', 'mercy', 'worser'], 
    ['caeser', 'mercy', 'worser'], 
    ['antony', 'caeser', 'mercy'], 
    ['angels', 'fools', 'fear', 'in', 'rush', 'tread', 'where'], 
    ['angels', 'fools', 'fear', 'in', 'rush', 'tread', 'where'], 
    ['angels', 'fools', 'in', 'rush', 'tread', 'where'], 
    ['fools', 'fear', 'in', 'rush', 'tread', 'where']]

document_num=0
postional_index={}

for document in documents:
    for positional , term in enumerate(document):


        if term in postional_index:

            postional_index[term][0] = postional_index[term][0]=1

            if document_num in postional_index[term][1]:
                postional_index[term][1][document_num].append(positional)

            else:
                postional_index[term][1][document_num]=[positional]


        else:
            postional_index[term]=[]

            postional_index[term].append(1)

            postional_index[term].append({})

            postional_index[term][1][document_num]=[positional]

    document_num +=1
print(postional_index)