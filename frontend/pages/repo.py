import streamlit as st
import requests

params = st.query_params

if "token" not in params:
    st.error("Please login first")
    st.stop()

token = params["token"]

username = st.text_input("Enter GitHub Username")

if username:

    response = requests.get(
        f"http://localhost:8000/repositories/{username}"
    )

    repos = response.json()

    selected_repo = st.selectbox(
        "Select Repository",
        [repo["name"] for repo in repos]
    )

    value=""
    if st.button("Analyze"):

        response = requests.post(
            "http://localhost:8000/analysis",
            params={
                "owner": username,
                "repo": selected_repo
            }
        )

        result = response.json()

        st.markdown(result["analysis"])
        

        
    
    
