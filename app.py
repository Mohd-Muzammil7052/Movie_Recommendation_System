import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?language=en-US&api_key=06a13a84fe2d142dfca0ad5b9586cafb'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" +  data['poster_path']

def recommend(movie):
    ind = movies[movies['title'] == movie].index[0]
    distances = similarity[ind]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x : x[1])[1:6]

    recommended_movies = []
    recommend_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommend_movies_poster

st.title("Movie Recommender System")

option = st.selectbox(
    "Enter the Name of the Movie",
    movies['title'].values,
)

if st.button('Recommend'):
    names,posters = recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader(names[0])
        st.image(posters[0])

    with col2:
        st.subheader(names[1])
        st.image(posters[1])

    with col3:
        st.subheader(names[2])
        st.image(posters[2])
        
    with col4:
        st.subheader(names[3])
        st.image(posters[3])

    with col5:
        st.subheader(names[4])
        st.image(posters[4])
        
