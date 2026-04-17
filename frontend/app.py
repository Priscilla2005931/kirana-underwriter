import streamlit as st

st.title("Kirana Store Underwriter")

st.write("Upload images and enter location")

files = st.file_uploader("Upload images", accept_multiple_files=True)

lat = st.text_input("Latitude")
lon = st.text_input("Longitude")

if st.button("Analyze"):
    st.success("Processing... (ML coming next)")