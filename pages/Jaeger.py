import streamlit as st
from PIL import Image

questName = ["Acquaintence","The survivalist path - Unprotected, but dangerous","Tehe survivalist path - Thrifty","The survivalist path - Zhivchik","The Survivalist path - Wounded beast","The Survivalist path - Toguh guy","The survivalist path - Cold blooded","The survivalist path - Junkie","survival path - Eagle owl","The survivalist path - Combat medic","Huntsman path - Secured perimeter","Huntsman path - The trophy","Huntsman path - Woods cleaning","Huntsman path - Controller","Huntsman path - Sellout","Huntsman path - Woods keeper","Huntsman path - Evil watchman","Huntsman path - Justice","Huntsman path - Sadist","Huntsman path - Eraser - Part 1","Huntsman path - Eraser - Part 2","Ambulance","Shady business","Nostalgia","Fishing place","Courtest visit","Hunting trip","Reserve","Tarkov shooter - Part 1","Tarkov shooter - Part 2","Tarkov shooter - Part 3","Tarkov shooter - Part 4","Tarkov shooter - Part 5","Tarkov shooter - Part 6","Tarkov shooter - Part 7","Tarkov shooter - Part 8","Huntsman path - Factory cheif","Pest control","Swift one","The hermit","Huntsman path - Outcast","Cease fire","The delicious sausage","Broadcast - Part 3","Broadcast - Part 4","The Huntsman Path - Administratpr"]
questInfo = ["Turn in food to Jaeger","Kill 5 scavs withput body armor on woods","Stash food in a bunker","Spend 5 minutes dehydrated","Kill 3 scavs while in pain","Kill 3 scavs in a single woods raid with out medicine","Eliminate 2 PMC's with a headshot","Kill 20 scavs on woods while under a stimulant effect","Kill 6 scavs at night","Reach level 5 vitality","Kill 8 PMC's in the factory office area","Kill Reshala and turn his gun in","Kill 30 scavs","Kill 2 PMC's while they are flashed","Kill Killa","Kill Shturman","Kill 7 PMC's in dorms","Kill Reshala's guards","Kill Sanitar","Kill Glukhar","Kill 6 raiders","Turn in medical supplies","Turn in 3 flash drives","Give Jaeger a family photo album","Turn in 2 labs cards","Find all the houses on shoreline","Kill sterman with the specified requirements","Fin the food storeage on Reserve","Kill scavs with a mosin","Kill more scavs with a mosin","Kill 3 PMC's with a mosin",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,]

st.title("Jaeger")

image = Image.open('Jaeger_Portrait.webp')
st.image(image)

for i in range(len(questName)):
    st.title(questName[i])
    st.write(questInfo[i])