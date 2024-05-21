import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load datasets
movies = pd.read_csv('Dataset/tmdb_5000_movies.csv')
credits = pd.read_csv('Dataset/tmdb_5000_credits.csv')

# Merge datasets
merged_movies = movies.merge(credits, on="title")

# Select relevant columns
merged_movies = merged_movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Drop rows with missing values
merged_movies.dropna(inplace=True)

# Convert string representation of lists to lists
def convert(obj):
    return [item['name'] for item in ast.literal_eval(obj)]

merged_movies['genres'] = merged_movies['genres'].apply(convert)
merged_movies['keywords'] = merged_movies['keywords'].apply(convert)

def convert3(obj):
    return [item['name'] for item in ast.literal_eval(obj)][:3]

merged_movies['cast'] = merged_movies['cast'].apply(convert3)

def fetch_director(obj):
    return [item['name'] for item in ast.literal_eval(obj) if item['job'] == 'Director']

merged_movies['crew'] = merged_movies['crew'].apply(fetch_director)

# Preprocess overview column
merged_movies['overview'] = merged_movies['overview'].apply(lambda x: x.split())

# Remove spaces from words
merged_movies['genres'] = merged_movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
merged_movies['keywords'] = merged_movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
merged_movies['cast'] = merged_movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
merged_movies['crew'] = merged_movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create 'tags' column
merged_movies['tags'] = merged_movies['overview'] + merged_movies['genres'] + merged_movies['keywords'] + merged_movies['cast'] + merged_movies['crew']

# Select relevant columns
new_df = merged_movies[['movie_id', 'title', 'tags']]

# Convert 'tags' into string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Stem words
ps = PorterStemmer()
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join([ps.stem(word) for word in x.split()]))

# Convert 'tags' to lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# Vectorize 'tags' using CountVectorizer
cv =  CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

# Define function to recommend movies
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

# Test recommendation function
recommend('Avatar')

# Save data and similarity matrix
pickle.dump(new_df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
