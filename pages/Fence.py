import streamlit as st
from PIL import Image

questName = ["The collector"]
questInfo = ["Turn in every streamer item with the status found in raid"]

st.title("Fence")

image = Image.open('Fence_Portrait.webp')
st.image(image)

for i in range(len(questName)):
    st.title(questName[i])
    st.write(questInfo[i])