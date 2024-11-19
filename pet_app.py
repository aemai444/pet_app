import streamlit as st
import requests

st.header("Welcome to my pet page",
         divider="rainbow")


def get_cat_image():
    url = "https://cataas.com//cat/gif"
    contents = requests.get(url)

    return contents.content

def get_dog_image_url():
    url = "https://random.dog/woof.json"
    contents = requests.get(url).json()
    dog_image_url = contents["url"]

    return dog_image_url

c1,c2 = st.columns(2)
with c1:
    cat_button = st.button("click here for a cat")
    if cat_button:
        cat_image =get_cat_image()
        st.image(cat_image, width=300, caption="look at this cutie")

with c2:
    dog_button = st.button("click here for a cute dog")
    if dog_button:
        dog_image_url = get_dog_image_url()

        #if the url ends with mp4, it keeps fetching new url
        while dog_image_url[-4:] == ".mp4":
            dog_image_url = get_dog_image_url()

        st.image(dog_image_url, width=300, caption="look at this cutie")
