import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = pd.read_csv("data/model_input.csv",delimiter=";")
# remove rows where lcpeak_avg or lceq_avg is 0
data = data[data['lcpeak_avg'] != 0]
data = data[data['lceq_avg'] != 0]
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


st.title('MDA_Switzerland - Data Science Project 🇨🇭🇨🇭')

# create a bar chart showing lcpeak_avg by day of week
st.dataframe(data)

st.write("Hello World")