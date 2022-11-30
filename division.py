import streamlit as st
import pandas as pd
st.write("""
Division of two numbers
""")
st.header('Enter the numbers')

def user_input_features():
  num1 = st.number_input("NUM1", min_value=0,max_value=10000000000, step=1)
  num2 = st.number_input("NUM2", min_value=1,max_value=100000000, step=1)

  data = { 'NUM1': num1,
           'NUM2':num2}
  features = pd.DataFrame(data, index=[0])
  return features

df = user_input_features()
st.header('Division : ')
st.write(df["NUM1"]/df["NUM2"])
