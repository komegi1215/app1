import requests
from send_email import send_email
import streamlit as st


api = "facc72f4-c06a-49d3-b2dc-49cbe6950cdd"

url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

response1 = requests.get(url)
data = response1.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "img.png"
response2 = requests.get(image_url)
if image_url.startswith("http"):
    response2 = requests.get(image_url)
    with open(image_filepath, 'wb') as file:
        file.write(response2.content)
    st.image(image_filepath)
else:
    st.write("Image URL not found")

st.title(title)
st.image(image_filepath)
st.write(explanation)
