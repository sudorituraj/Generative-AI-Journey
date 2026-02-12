import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

#taking input 

name = st.text_input("What is your name: ")

age = st.slider("Select Your Age: ",0,100,18) # initialize , final, min
st.write("Your age is",age)

options= ['Python','Java',"C++","PHP"]
choice = st.selectbox("Choose your Favourite Language", options)
st.write("You SElected",choice)


if name: 
    st.write("Hello",name)
    
    
data = {
    "name":["Alex","Adam","Clerk","Smithy"],
    "age": [29,23,17,28],
    "City":["London","Canbera","New York","Washingkton DC"]
    
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file= st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)