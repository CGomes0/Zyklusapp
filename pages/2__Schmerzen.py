import streamlit as st
import pandas as pd
import altair as alt
from jsonbin import load_data, save_data


#jsonbin
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


st.title("Schmerzen Auswertung")

#barchart with pandas for pain
file_pain=load_data(api_key, bin_id)


pain = "pain"
pain_values = [day[pain]for key, day in file_pain.items() if pain in day]   #getting values from nested dictionary

dif = pd.DataFrame({
    "Schmerzen" : pain_values,
    "Tag" : file_pain.keys()
    })


st.line_chart(dif, x= "Tag", y = "Schmerzen")


