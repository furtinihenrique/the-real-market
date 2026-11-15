import streamlit as st
import json
import requests
import random as rd
from datetime import datetime
from PIL import Image

def positive_variation(variation):
    if(variation > 0):
        return True
    else:
        return False

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
        api_url = "http://127.0.0.1:8000/brent/latest"
        api_request = requests.get(api_url).json()
        st.subheader(api_request["last_price"])
        positive = positive_variation(api_request["variation"])
        if positive:
            st.write(f":green[+{api_request["variation"]}%]")
        else:
            st.write(f":red[-{api_request["variation"]}%]")
        
        st.button("Check Brent", width="stretch")
    with col2:
        st.header("GOLD")
        st.subheader("Coming Soon")
        #st.write(f":green[+1.87%]")
        st.button("Check GOLD", width="stretch")
    with col3:
        st.header("S&P500")
        st.subheader("Coming Soon")
        #st.write("Coming Soon")
        st.button("Check S&P500", width="stretch")
    with col4:
        st.header("EUR/USD")
        st.subheader("Coming Soon")
        #st.write(f":red[-1.87%]")
        st.button("Check EUR/USD", width="stretch")
        
    st.write("Real Brent Oil + Demonstrative only")

st.button("Analyze the market ➔", width="stretch")
st.divider()

st.divider()

st.divider()
