import streamlit as st
from datetime import datetime

time = datetime.now()

st.set_page_config("The Real Market", "random", "wide")

st.title("The Real Market")

if time.hour > 5 and time.hour < 12:
    st.write("Good Morning!")
elif time.hour > 12 and time.hour < 5:
    st.write("Good Morning!")
elif time.hour > 5 and time.hour < 8:
    st.write("Good Evening!")
else:
    st.write("Good Night!")

st.write("Simplicity and market, here, now")

st.divider()

st.divider()

st.divider()

st.divider()
