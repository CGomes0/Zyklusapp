import streamlit as st
from datetime import datetime, date, timedelta 
from jsonbin import load_data, save_data


#jsonbin
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


#login






st.title("Mein Zyklustagebuch")

#date used as key value in json
date = st.date_input("Speicherdatum", date.today())

#date input on calendar
date_zyklus = st.date_input( 
    "Wann war mein letzter Zyklus?",
    date.today())

#ISO date to european date
european_format = "%d.%m.%Y"            
st.write('Letzter Zyklus war am:', datetime.strftime(date_zyklus, european_format))

#next menstruation date calculated
next_date = date_zyklus + timedelta(days=28)
st.write("Nächster Zyklus ist am", datetime.strftime(next_date, european_format))


#Eingabe Stärke der Schmerzen
pain = st.slider('Wie stark sind deine Schmerzen? 1 schwach und 10 stark', 0, 10)
st.write("Sie haben eine Stärke von", pain)

st.text("Ich habe heute folgende Medikamente genommen:")

#Hauptteil der App, Eingabe der Beschwerden
col1, col2, col3, col4 = st.columns(4)

with col1:
    medi1 = st.selectbox(
        "Morgen",
        ("-","Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
        )
    
with col2:
    medi2 = st.selectbox(
        "Mittag",
        ("-","Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
        )
    
with col3:
     medi3 = st.selectbox(
         "Abend",
         ("-","Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
         )

with col4:
    medi4 = st.selectbox(
        "Vor dem Schlafen",
        ("-","Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
        )
    

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


col5, col6, col7 = st.columns(3)

with col5:
    feeling = st.radio(
        "Wie fühlst du dich?", 
        ("😀", "😐", "😭", "😡"))

with col6:
    intensity = st.radio(
        "Wie stark sind die Menstruationsblutungen?",
        ("Keine","Leicht", "Mittel", "Stark"))
    
with col7:    
    notice= st.text_area(
        "Meine Notizen:")
    

    
col8, col9 = st.columns(2)

with col8:
    ovutest = st.radio(
        "Habe ich einen Ovulationstest gemacht? Wenn ja, was war das Resultat?", 
        ("Keinen Test gemacht", "Positiv", "Negativ"))

with col9:
    temperatur= st.text_input(
        "Meine gemessene Temperatur in °C:",
        "")
    

def save():
    
    
    data = load_data(api_key, bin_id)
    
    data.update({
            str(date): {
                'pain': pain,
                'medi1': medi1,
                'medi2': medi2,
                'medi3': medi3,
                'medi4': medi4,
                'feeling': feeling,
                'intensity': intensity,
                'notice': notice,
                'ovutest': ovutest,
                'temperatur': temperatur
            }
        })
    
    save_data(api_key, bin_id, data)
        
        
           
    return 
button = st.button('Speichern',on_click=save)


