import streamlit as st
import pandas as pd
import numpy as np
import time

"""
# My first app
Here's our first attempt at using data to create a table:
"""

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0))
st.line_chart(df)


@st.cache(suppress_st_warning=True)
def set_map_data():
    time.sleep(2)
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    return map_data

st.map(set_map_data())


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option