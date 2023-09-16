import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
similarity=pd.DataFrame(similarity)


def fetch_movie_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US" .format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5N2MyYTM0NzljN2IyZmZlZDdhNTQ2MmFjNDg1MTUzNyIsInN1YiI6IjY1MDVkYTgwZmEyN2Y0MDEwYzQ5ZjA2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SPp4OoyV9cbCt3RNwoOIMcd8WzkamMawx_YaYZzj1ig"
    }

    response = requests.get(url, headers=headers)
    response=response.json()
    
    
    image_path='https://image.tmdb.org/t/p/original'+response['poster_path']
    
    return image_path



def recommend(movie):
    
    movie_index=movies[movies['title']==movie].index[0]
    similar_movie_list=list(enumerate(similarity[movie_index]))
    similar_movie_list=sorted(similar_movie_list,reverse=True,key=lambda x : x[1])[1:6]
    recommendation=[]
    recommended_poster=[]
    for i in similar_movie_list:
        recommendation.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_movie_poster(movies.iloc[i[0]].id))
    
        
    return recommendation,recommended_poster







st.title('Movie Recommender System')

option = st.selectbox(
    'Type/ Select a movie that you like',
    movies['title'].values)


if st.button("Recommend"):

    names,poster=recommend(option)
    
    col1 ,col2 , col3 , col4 , col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
