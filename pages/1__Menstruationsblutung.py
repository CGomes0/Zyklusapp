import streamlit as st
import pandas as pd
import altair as alt
import json


st.title("Menstruationsblutung Auswertung")

#barchart with pandas for Menstruationblutung
with open("data.json", "r")as file:
    file_intensity = json.load(file)
    
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