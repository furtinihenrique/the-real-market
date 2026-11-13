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
    st.caption((phrases[number]["phrase"]))
    st.caption(phrases[number]["author"])

st.write("Simplicity and market, here, now")

st.divider()

st.divider()

st.divider()

st.divider()
