import streamlit as st
import pandas as pd
import altair as alt
from jsonbin import load_data, save_data


#jsonbin
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


st.title("Menstruationsblutung Auswertung")

#barchart with pandas for Menstruationblutung
file_intensity=load_data(apy_key, bin_id)
    
intensity = "intensity"
bleeding = [day[intensity]for key, day in file_intensity.items() if intensity in day]   #getting values from nested dictionary
    

daf = pd.DataFrame({
    "Intensität" : bleeding,
    "Tag" : file_intensity.keys()
    })


bar_chart = alt.Chart(daf).mark_line().encode(
    x = "Tag",
    y = alt.Y("Intensität", scale=alt.Scale(reverse=True)))

st.altair_chart(bar_chart, use_container_width = True)
