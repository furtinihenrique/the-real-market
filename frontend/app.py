import streamlit as st
import json
import random as rd
from datetime import datetime
from PIL import Image

time = datetime.now()

image = Image.open("favicon.png")
st.set_page_config("The Real Market", image, "wide")

st.title("The Real Market")

if time.hour > 5 and time.hour < 12:
    st.write("Good Morning!")
elif time.hour > 12 and time.hour < 5:
    st.write("Good Morning!")
elif time.hour > 5 and time.hour < 8:
    st.write("Good Evening!")
else:
    st.write("Good Night!")

with open("phrases.json", "r") as file:
    phrases = json.load(file)
    number = rd.randrange(0,14)
    st.caption(f":blue[‘{phrases[number]["phrase"]}’]")
    st.caption(phrases[number]["author"])

st.write("Simplicity and market, here, now.")

st.divider()

st.header("Market Overview")
col1,col2,col3,col4 = st.columns(4, border=True)
with st.container(border=True):
    with col1:
        st.header("Brent Oil")
        st.subheader("98.087")
        st.write(f":green[+1.87%]")
        st.button("Check Brent", width="stretch")
    with col2:
        st.header("GOLD")
        st.subheader("129.988")
        st.write(f":green[+1.87%]")
        st.button("Check GOLD", width="stretch")
    with col3:
        st.header("S&P500")
        st.subheader("7573.060")
        st.write(f":green[+1.87%]")
        st.button("Check S&P500", width="stretch")
    with col4:
        st.header("EUR/USD")
        st.subheader("0.900")
        st.write(f":red[-1.87%]")
        st.button("Check EUR/USD", width="stretch")
        
    st.write("Demonstrative only")

st.button("Analyze the market ➔", width="stretch")
st.divider()

st.divider()

st.divider()
