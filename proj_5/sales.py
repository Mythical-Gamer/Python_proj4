import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **Pokemon cards sales**
---
''')
#reading file
df = pd.read_csv('/content/Chilling Reign Sales Data.csv')
st.write(df)

st.title("Sales Data Visualization")


# Line Chart
st.subheader("Line Chart")
fig_line, ax_line = plt.subplots()
ax_line.plot(df['Date Sold'], df['Price Sold'])
ax_line.set_ylabel('Price Sold')
ax_line.set_xlabel('Date Sold')
st.pyplot(fig_line)

# Bar Chart
st.subheader("Bar Chart")
fig_bar, ax_bar = plt.subplots()
ax_bar.bar(df['Price Sold'], df['Quantity'])
ax_bar.set_xlabel('Price Sold')
ax_bar.set_ylabel('Quantity')
st.pyplot(fig_bar)

# Pie Chart
st.subheader("Pie Chart")
categories = df['Quantity'].value_counts()
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(categories, labels=categories.index, autopct='%1.1f%%')
st.pyplot(fig_pie)