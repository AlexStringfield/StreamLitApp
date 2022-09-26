import streamlit
import pandas as pd

streamlit.title('Matthew Smells!')


streamlit.header('Really really bad')
streamlit.text('It'+chr(39)+'s a real problem, kind of smells like:')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('with just a hint of 🥣 🥗 🐔 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.columns(1)))

streamlit.dataframe(my_fruit_list)
