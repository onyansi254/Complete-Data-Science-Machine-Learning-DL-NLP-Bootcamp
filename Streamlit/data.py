import streamlit as st
import pandas as pd
import os

# Load or create profiles CSV
DATA_FILE = "profiles.csv"
if os.path.exists(DATA_FILE):
    profiles_df = pd.read_csv(DATA_FILE)
else:
    profiles_df = pd.DataFrame(columns=["Name", "Age", "Gender", "Interests"])

# App Title
st.title("💖 Dating Scenes")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Register Profile", "Discover Profiles"])

if page == "Register Profile":
    st.header("Create Your Dating Profile")
    
    name = st.text_input("Your Name")
    age = st.slider("Your Age", 18, 100, 25)
    gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
    interests = st.text_area("Your Interests (comma-separated)", placeholder="e.g., Music, Hiking, Cooking")

    if st.button("Save My Profile"):
        if name.strip() == "" or interests.strip() == "":
            st.error("Please fill out all fields.")
        else:
            new_profile = pd.DataFrame([{
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Interests": interests
            }])
            profiles_df = pd.concat([profiles_df, new_profile], ignore_index=True)
            profiles_df.to_csv(DATA_FILE, index=False)
            st.success("Your profile has been saved successfully!")

elif page == "Discover Profiles":
    st.header("Discover Other Profiles")
    
    if not profiles_df.empty:
        min_age = st.slider("Minimum Age", 18, 100, 18)
        max_age = st.slider("Maximum Age", min_age, 100, 35)
        
        filtered = profiles_df[(profiles_df["Age"] >= min_age) & (profiles_df["Age"] <= max_age)]
        
        if not filtered.empty:
            for idx, row in filtered.iterrows():
                st.subheader(f"{row['Name']} ({row['Age']}) - {row['Gender']}")
                st.write("Interests:", row['Interests'])
                st.markdown("---")
        else:
            st.info("No profiles found within this age range.")
    else:
        st.warning("No profiles registered yet!")
