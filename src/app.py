import pickle
import numpy as np
import pandas as pd
import streamlit as st

PASSENGER =  {1: "1st", 2: "2nd", 3: "3rd"}
SEX =  {0: "female", 1: "male"}
EMBARKED =  {0: "C", 1: "S", 2: "Q"}

def model(features):
    model = pickle.load(open('./models/titanic_model.pkl', 'rb'))
    cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    final_features = pd.DataFrame(np.array(features).reshape(1,7), columns=cols)
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return output

def format_func_passenger(option):
    return PASSENGER[option]

def format_func_sex(option):
    return SEX[option]

def format_func_embarked(option):
    return EMBARKED[option]

st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
st.title('Titanic survival prediction')
st.markdown("<description>The sinking of the Titanic is one of the most infamous shipwrecks in history. " + 
    "On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding" +
    "with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of " +
    "1502 out of 2224 passengers and crew. While there was some element of luck involved in surviving, it seems some" +
    " groups of people were more likely to survive than others. </description>", unsafe_allow_html=True)
st.sidebar.title('Select the parameters to analyze survival prediction')
pclass = st.sidebar.selectbox("Passenger Class" ,options=list(PASSENGER.keys()), format_func=format_func_passenger)
sex = st.sidebar.selectbox("Passenger Sex" ,options=list(SEX.keys()), format_func=format_func_sex)
age = st.sidebar.slider('Age', min_value=1, max_value=90, step=1)
sibsp = st.sidebar.slider('Number of siblings/spouses aboard', min_value=1, max_value=10, step=1)
parch = st.sidebar.slider('Passenger Parch', min_value=1, max_value=5, step=1)
fare = st.sidebar.number_input('Passenger Fare', min_value=1, max_value=20000)
embarked = st.sidebar.selectbox("Passenger Embarked" ,options=list(EMBARKED.keys()), format_func=format_func_embarked)
if st.sidebar.button("Predict"):
    features = [pclass, sex, age, sibsp, parch, fare, embarked ]
    result = model(features)
    st.header('Would you survive?')
    st.subheader('YES' if result else 'NO')