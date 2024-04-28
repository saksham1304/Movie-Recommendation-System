import streamlit as st
import pickle
import pandas as pd
movi=pickle.load(open('movdata.pkl','rb'))
sim=pickle.load(open('sim.pkl','rb'))
movies=pd.DataFrame(movi)
def similarmovies(name):
    index = movies[movies['title'] == name].index[0]
    dis = sorted(list(enumerate(sim[index])),reverse=True,key = lambda x: x[1])
    re_mov=[]
    for i in dis[1:6]:
        re_mov.append(movies.iloc[i[0]].title)
    return re_mov

st.title("A Movie Recommandation System By Mridul Gupta")
st.header("Set Of Over 1k Movies")
st.subheader("Based On Content Based Recommandation")
option=st.selectbox("Type The Name Of The Movie ",movies['title'].values)
if st.button('Recommand'):
    re=similarmovies(option)
    for i in re:
        st.write(i)
st.caption("Dataset By Movielens")