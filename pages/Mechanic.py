import streamlit as st
from PIL import Image

questName = ["Introduction","Gunsmith - Part 1 - 25","Farming - Part 1","Farming - Part 2","Farming - Part 3","Farming - Part 4","Signal - Part 1","Signal - Part 2","Signal - Part 3","Signal - Part 4","The Chemistry Closet","Bad Habit","Scout","Insider","Psycho Sniper","Import","Fertilizers","A Shooter Born In Heaven","Surplus goods","Back door","Energy Crisis","Broadcast","Broadcast - Part 2","Surveillance","Watching You"]
questInfo = ["Find Jaeger on woods","Modify all weapons to mechanics specifications","Fix the control boards in the factory","Find in raid 2 powercords, 4 t-plugs, and 2 circuit boards","Find the package of graphics cards and extract","Turn in 3 found in raid graphics cards and 8 cpu fans","Mark 2 antennas on Shoreline","Turn in 3 found in raid cpu's, batteries, circuit boards ,and broken phones","Place 3 signal jammers on Shoreline","Reach memory skill level 4","Go to east 110 in the health resort and extract","Find cigaretts in raid and turn them in","Go to all extracts on factory and leave","Get level 3 Prapor","Obtain level 10 sniper skill and kill 5 pmc's with a bolt action in 1 raid","Turn in found in raid UHF RFID readers and VPX and turn them in","Find 5 wires and capacitors in raid and turn them in","Kill 5 pmc's on every map with a headshot from a bolt action rifle","Turn in a navigation system to Mechanic","Extract through D2 on Reserve","Mark all fuel containers on Lighthouse","Place a signal jammer in the operating room on lighthouse","Locate the broadcaster in Streets if tarkov","Hand over information about the vehicle movement","Locate the surveillance spot on Streets of tarkov"]

st.title("Mechanic")

image = Image.open('Mechanic_Portrait.webp')
st.image(image)

for i in range(len(questName)):
    st.title(questName[i])
    st.write(questInfo[i])