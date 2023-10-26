import streamlit as st
from PIL import Image

questName = ["Supplier","The Extortionist","Stirrup","What's on the flash drive","Golden Swag","Chemical - Part 1","Chemical - Part 2","Chemical Part - 3","Chemical - Part 4","Rigged Game","Loyalty Buyout","Friend from the West - Part 1","Friend From the West - Part 2","Vitamins - Part 1","Vitamins - Part 2","Lend Lease - Part 1","Informed Means Armed","Chumming","Silent Caliber","Flint","Bullshit","Setup","Safe Corridor","Night Sweep","Long Road","Missing Cargo","House Arrest - Part 1","Debtor"]
questInfo = ["Handover 1 3m body armour and 1 toz shotgun","Find the unnown key, use it to find the documents and extract","Kill 3 pmc's with pistols","Find 2 in raid flash drives","Find the golden lighter in room 303 and stash it in the cabin","Find documents on the train and survive", "Find a letter and flash drive in dorm 220 and extract","Find the syringe in the factory and extract","Mark the van on customs","Mark 3 medical containers on shoreline","Hand over 1 million roubles","Eliminate 7 USEC pmc's and hand over 7 BEAR and USEC dogtags","Hand over $6000 usd","Hand over 1 million roubles","Find 3 medical bloodsets and 4 respirators","Find 3 motor controllers 2 gyroscopes and extract","Place 3 wifi cameras","Stash 9 gold chains and kill 5 pmc's on Interchange from 22:00 to 10:00","While using a suppressed shotgun kill 20 scavs and 10 pmc's","Earn level 6 stress resistance","Plant a fake flash drive, sv-98 rifle, and a roller wrist watch in dorms and do not kill any scav","Kill 15 pmc's while wearing specific gear on customs","Eliminate 0 scavs in the underground warehouse on reserve","Find 12 unusual knives in raid and hand them over to skier","Kil 15 scavs on the main road on lighthouse","Locate the crashed helicopter and inteligence folder, and hand it over","Locate where the missing group was held captive and extract","Find the debtor and extract"]

st.title("Skier")

image = Image.open('Skier_Portrait.webp')
st.image(image)

for i in range(len(questName)):
    st.title(questName[i])
    st.write(questInfo[i])