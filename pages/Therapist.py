import streamlit as st
from PIL import Image

questName = ["Shortage","Sanitary Standards Part 1","Sanitary Standards Part 2","Operation Aquarius Part 1","Operation Aquarius Part 2","Painkillers","Pharmacist","Supply Plans","General Wares","Colleagues - Part 1","Colleagues - Part 2","Colleagues - Part 3","Car Repair","Health Care Privacy Part 1","Health Care Privacy Part 2","Health Care Privacy Part 3","Health Care Privacy Part 4","Health Care Privacy Part 5","Postman Part 2","Out of Curiosity","Trust Regain","Hippocratic Vow","Private Clinic","Trust Regain","Decontamination Services","An Apple A Day Keeps the Doc Away","Disease history","Seaside Vacation","Lost Contact","Population Census","Dangerous Road","Urban Medicine"]
questInfo = ["Turn in 3 found in raid salewa's","Turn in 1 found in raid gas analyzer","Turn in 2 found in raid gas analyzer's","Visit dorm room 206 and extract","Kill 15 scavs on customs","Turn in 4 found in raid morphines","Find the case in dorm room 114 and extract","Find the secure folder on woods and extract","Turn in 15 found in raid cans of tushonka","Find 3 bodies on shoreline and extract","Obtains Sanitar's surgery kit and ophtalmoscope and extract","Hand over a found in raid AHF1-M stim, 3-(b-TG) stim and green and blue keycard","Hand over 4 found in raid car batteries and 8 spark plugs","Mark 3 ambulances on shoreline","Find the information in room 306 of the health resorts west wing and extract","Find a blood sample on woods and extract","Reach health skill level 4","Dropoff 3 kite gunpowder in the factory","Find a letter on a dead scav on factory and extract","Mark a chemical transporter on ctustoms","Drop off 3 kite gunpowder in the factory","Handover 5000 U.S. dollars","Handover 1 opthalmoscope and 1 ledx found in raid","Reach health skill level 10","Kill 30 scavs on interchange from less than 60 meters while wearing specific gear","Handover 400k roubles","Turn in 2 medical journals","Find the informants briefcase and hand it over","Find the lost group and extract","Obtain the journal and hand it over","Survive and extract through the car extract on streets of tarkov","Locate the chemical labratory, obtain the drug sampes, hand them over"]

st.title("Therapist")

image = Image.open('Therapist_Portrait.webp')
st.image(image)

for i in range(len(questName)):
    st.title(questName[i])
    st.write(questInfo[i])