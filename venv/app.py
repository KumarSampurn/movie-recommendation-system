import streamlit as st
import pickle
import pandas as pd

movie_dict=pickle.load(open('../movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('../similarity.pkl','rb'))
similarity=pd.DataFrame(similarity)




def recommend(movie):
    
    movie_index=movies[movies['title']==movie].index[0]
    similar_movie_list=list(enumerate(similarity[movie_index]))
    similar_movie_list=sorted(similar_movie_list,reverse=True,key=lambda x : x[1])[1:6]
    recommendation=[]
    for i in similar_movie_list:
        recommendation.append(movies.iloc[i[0]].title)
    
        
    return recommendation





st.title('Movie Recommender System')

option = st.selectbox(
    'Type/ Select a movie that you like',
    movies['title'].values)


if st.button("Recommend"):

    recommendation=recommend(option)
    
    for i in recommendation:
        st.write(i)
