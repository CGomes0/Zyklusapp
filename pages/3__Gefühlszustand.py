import streamlit as st
import pandas as pd
import altair as alt
from jsonbin import load_data, save_data


#jsonbin
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


st.title("Gefühlszustand Auswertung")

#barchart with pandas for feelings
file_feeling=load_data(api_key, bin_id)


feel = "feeling"
feelings = [day[feel]for key, day in file_feeling.items() if feel in day]   #getting values from nested dictionary

dif = pd.DataFrame({
    "Gefühlszustand" : feelings,
    "Tag" : file_feeling.keys()
    })


st.line_chart(dif, x= "Tag", y = "Gefühlszustand")
