import streamlit as st
from PIL import Image

questName = ["Only buisness","Make ULTRA Great Again","Big Sale","The Blood War Part 1","Dresses To Kill","Gratitude","Sales Night","Hot Delivery","Scavenger","Database Part1","Database Part 2","Minibus","Sew It Good Part 1","Sew It Good Part 2","Sew It Good Part 3","Sew It Good Part 4","The Blood Of War Part 2","The Blood Of War part 3","The Key To Success","Living High Is Not A Crime Part 1","Living High Is Not A Crime Part 2","Charisma Brings Success","No Fuss Needed","Supervisor","The Stylish One","Textiles","Fuel Matter","Inventory Check","Long Line","Booze","Calibration","The Courier","Corporate Secrets","Communication Difficulties","Ballet Lover","Audiophile","Audit","Harley Forever"]
questInfo = ["Reach level 2 Ragman","Kill 25 scavs on Interchange","Visit the main stores of the mall","Mark the 3 gas tanks on Interchange","Hand over 2 Ushanka hats and 2 Cowboy hats","Leave specified clothing in a specified place","Survive 7 Interchange raids","Stash your gear in a specified place","Reach search skill 9","Obtain the buisness manifests on Interchange","Obtain buisness cargo routes","Mark the mini busses on Interchange","Turn in a found in raid Shmask mask and a pilgrim pack","Hand over a damaged and new Gzhel","Hand over a damaged and new 6b43","Turn in 2 blackrock rigs and 2 wartech rigs","Turn in 4 fuel conditioners","Mark 3 fuel stashes on woods","Handover the handbooks","Turn in all specified treasure items","Turn in more treasure items","Reach level 10 charisma","Reach level 3 Therapist","Hand over Goshan's register key","Kill killa 50 times","Turn in clothing materials","Mark the fuel tankers on Reserve","Find all arsenal's on Reserve","Kill 30 pmc's inside the Interchange mall","Turn in a lot of booze","Kill 20 pmc's from 100 meters away","Stash a thermal scope on Customs","Locate and hand over extracted data","Explore the lighthouse area","Locate an appartment","Locate the musicians guitar pick and turn it in","Obtain financial records","Locate and Mark all motercycles"]

st.title("Ragman")

image = Image.open('Ragman_Portrait.webp')
st.image(image)

for i in range(len(questName)):
    st.title(questName[i])
    st.write(questInfo[i])