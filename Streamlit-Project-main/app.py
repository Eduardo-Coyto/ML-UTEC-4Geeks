import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as px 
import streamlit as st

@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/rfordatascience/' + \
    'tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv'
    df = pd.read_csv(url)
    df_interim = df.copy()
    df_interim = df_interim[['total_cup_points',
                                'species',
                                'country_of_origin',
                                'variety',
                                'aroma',
                                'aftertaste',
                                'acidity',
                                'body',
                                'balance',
                                'sweetness',
                                'altitude_mean_meters',
                                'moisture']]
    df_interim = df_interim.dropna()
    df_interim['species'] = pd.Categorical(df_interim['species'])
    df_interim['country_of_origin'] = pd.Categorical(df_interim['country_of_origin'])
    df_interim['variety'] = pd.Categorical(df_interim['variety'])
    df_interim['specialty'] = df_interim['total_cup_points'].\
        apply(lambda x: 'Yes' if x>82.43 else 'No')
    df = df_interim.copy()
    return df

df_ch = load_data()

st.title('Coffee dataset explorer')
st.subheader('Dataframe')
st.dataframe(df_ch)
st.subheader('Histograms')
col1, col2 = st.columns(2)
fig1 = px.histogram(df_ch, x='aroma')
fig2 = px.histogram(df_ch, x='aftertaste')
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

# Heroku uses the last version of python, but it conflicts with 
# some dependencies. Low your version by adding a runtime.txt file
# https://stackoverflow.com/questions/71712258/