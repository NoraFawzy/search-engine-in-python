documents = [
    'antony brutus caeser cleopatra mercy worser',
    'antony brutus caeser calpurnia ',
    'mercy worser',
    'brutus caeser mercy worser',
    'caeser mercy worser',
    'antony caeser mercy ',
    'angels fools fear in rush to tread where',
    'angels fools fear in rush to tread where',
    'angels fools in rush to tread where',
    'fools fear in rush to tread where',
]
import pandas as pd
import numpy as np
from  sklearn.feature_extraction.text import TfidfVectorizer
vector = TfidfVectorizer()
x = vector.fit_transform(documents)
x = x.T.toarray()

df=pd.DataFrame(x,index=vector.get_feature_names_out())

# print(df)
query = 'antony brutus'

q = [query]

q_vector=vector.transform(q).toarray().reshape(df.shape[0])

similarty = {}

for i in range(10):
    similarty[i]=np.dot(df.loc[:,i].values,q_vector)/np.linalg.norm(df.loc[:,i]) * np.linalg.norm(q_vector)

print (similarty)

similarty_sorted=sorted(similarty.items(),key=lambda x: x[1])
for document, score in similarty_sorted:
    # if score >0.5:
        print('doc is :',document)
        print('similar scor=',score)
        