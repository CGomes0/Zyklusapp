import streamlit as st
import pandas as pd
import altair as alt
import json


st.title("Ovulationstest Auswertung")

#barchart with pandas for Ovutest
with open("data.json", "r")as file:
    file_ovutest = json.load(file)
    
ovu = "ovutest"
ovutests = [day[ovu]for key, day in file_ovutest.items() if ovu in day]   #getting values from nested dictionary
    
#sorting out all none ovutest
def ovu_not_none(ovutests):
    measured_ovutests = []
    for a in ovutests:
        if a != "Positiv" or "Negativ":
            measured_ovutests.append(a)
    return measured_ovutests

measured_ovu = ovu_not_none(ovutests)

daf = pd.DataFrame({
    "Ovaluationstest" : measured_ovu,
    "Tag" : file_ovutest.keys()
    })


bar_chart = alt.Chart(daf).mark_bar().encode(
    x = "Tag",
    y = alt.Y("Ovaluationstest", scale=alt.Scale(reverse=True)))

st.altair_chart(bar_chart, use_container_width = True)