import joblib
import streamlit as st
import difflib
import pandas as pd

#Load saved files
movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity.pkl")
movies = movies.reset_index(drop=True)

st.title('Movie Recommender')
movie_name = st.text_input('Enter your movie name')

if st.button('Recommend related movies'):
    titles_list = movies['title'].tolist()
    close_match = difflib.get_close_matches(movie_name, titles_list)

    if close_match:
        closest_match = close_match[0]
        movie_index = movies[movies.title == closest_match].index[0]
        similarity_score = list(enumerate(similarity[movie_index]))
        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
        st.subheader(f'Movies similar to {closest_match}')

        count = 0

        for movie in sorted_similar_movies[1:]:

            index = movie[0]

            title = movies[movies.index ==
                        index]['title'].values[0]

            if count < 30:
                st.write(f"{count+1}. {title}")
                count += 1
            else:
                break

    else:
        st.error("Movie not found.")