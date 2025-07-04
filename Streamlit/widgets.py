import streamlit as st

st.title("Dataing scenes")

name = st.text_input("Enter your name: ")

age=st.slider("Select your age:", 0, 100, 25)
st.write(f'You selected {age} years old.')

if st.button("Submit"):
    st.write(f"Hello, {name}! Welcome to the Dataing scenes app!")