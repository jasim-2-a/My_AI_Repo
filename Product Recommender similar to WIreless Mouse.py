import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = {
    'product_id': [1, 2, 3, 4, 5],
    'name': ['Wireless Mouse', 'Wired Mouse', 'Wireless Keyboard', 'Gaming Headset', 'Bluetooth Speaker'],
    'description': [
        'Wireless mouse with ergonomic design and long battery life',
        'Basic wired mouse with optical sensor',
        'Compact wireless keyboard with quiet keys',
        'Over-ear gaming headset with surround sound',
        'Portable Bluetooth speaker with rich bass and waterproof design'
    ]
}


df = pd.DataFrame(data)


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = df[df['name'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]
    product_indices = [i[0] for i in sim_scores]
    return df['name'].iloc[product_indices]


print("Products similar to 'Wireless Mouse':")
print(get_recommendations('Wireless Mouse'))
