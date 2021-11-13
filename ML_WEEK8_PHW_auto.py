
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
from numpy import dot

"""
get L2 norm of vector
"""
def L2(vec):
    result = 0
    for i in vec:
            result += i**2
    return np.sqrt(result)
"""
get cosine similariry from two vectors
"""
def cos_sim(vec1, vec2):
    return dot(vec1, vec2)/(L2(vec1)* L2(vec2))

def getResult(sentences, query):
    """
    Read documents and query as list
    """

    cvec = CountVectorizer(stop_words='english', min_df=3,max_df=0.9,ngram_range=(1,1))
    sentences.append(query)
    sf = cvec.fit_transform(sentences)
    """
    get tfidf with tf/idf table.
    """
    tf = pd.DataFrame(sf.toarray(),columns = cvec.get_feature_names())
    D = len(tf)
    df = tf.astype(bool).sum(axis=0)
    idf = np.log((D+1)/(df+1)) +1
    tfidf = tf * idf
    tfidf = tfidf / np.linalg.norm(tfidf, axis=1, keepdims=True)
    """
    get cosine similarity and sort by cosine similarity to show rank order
    """
    cos_sim_set = list()
    for i in range(5):
        cos_sim_set.append(cos_sim(tfidf.iloc[i,:],tfidf.iloc[5,:]))
    result = pd.DataFrame([x for x in zip(range(5),cos_sim_set)],columns=['document number','cosine similarity'])
    result.sort_values(by=['cosine similarity'],axis=0,inplace=True,ascending=False)

    print(result)
